---
author: Vahid Nasiri
source: .NET Tips
url: https://www.dntips.ir/post/3048
published: 2019-05-31
type: human
genre: technical-educational
provenance: attributed-excerpt
note: Representative excerpt from a third-party technical article, supplied in the conversation for false-positive testing. The full article remains at the source URL.
---

# C# 8.0 - Ranges & Indices — benchmark excerpt

[نوع Span](https://www.dntips.ir/post/2818/span-%d8%af%d8%b1-c-7-2) به همراه NET Core 2.1. ارائه شد. یکی از مهم‌ترین مزایای آن امکان دسترسی به قسمتی از حافظه (توسط متد Split آن)، بدون ایجاد سربار کپی یا تخصیص مجدد حافظه‌ای برای دسترسی به آن است. قدم بعدی، بسط این قابلیت به امکانات ذاتی زبان #C است؛ تحت عنوان ویژگی Ranges که امکان دسترسی مستقیم به بازه‌ای/قسمتی از آرایه‌ها، رشته‌ها و یا Spanها را میسر می‌کند.


**معرفی عملگر Hat**

برای دسترسی به آخرین عضو یک آرایه عموما از روش زیر استفاده می‌شود:


```csharp
```

```csharp
var integerArray = new int[3];
var lastItem = integerArray[integerArray.Length - 1];
```

یعنی از آخر شروع به شمارش کرده و 1 واحد از آن کم می‌کنیم (این عدد 1 را به‌خاطر داشته باشید) و یا اگر بخواهیم از LINQ استفاده کنیم می‌توان از متد Last آن استفاده کرد:


```csharp
```

```csharp
var integerList = integerArray.ToList();
integerList.Last();
```

همچنین اگر بخواهیم دومین عنصر از آخر آن‌را دریافت کنیم:


```csharp
```

```csharp
var secondToLast = integerArray[integerArray.Length - 2];
```

نیز مجددا از آخر شروع به شمارش کرده و 2 واحد، از آن کم می‌کنیم (این عدد 2 را نیز به‌خاطر داشته باشید).

این شمردن‌های از آخر در C# 8.0 توسط ارائه‌ی عملگر hat یا همان ^ که پیشتر کار xor را انجام می‌داد (و البته هنوز هم در جای خودش همین مفهوم را دارد)، میسر شده‌است:


```csharp
```

```csharp
var lastItem = integerArray[^1];
```

این قطعه کد یعنی به دنبال ایندکس X، از آخر آرایه هستیم.

**نکته‌ی مهم:** کسانیکه شروع به آموزش برنامه نویسی می‌کنند، مدتی طول می‌کشد تا عادت کنند که اولین ایندکس یک آرایه از صفر شروع می‌شود. در اینجا باید درنظر داشت که با بکارگیری «عملگر کلاه»، آخرین ایندکس یک آرایه از «یک» شروع می‌شود و نه از صفر. برای نمونه در مثال زیر به خوبی تفاوت بین ایندکس از ابتدا و ایندکس از انتها را می‌توانید مشاهده کنید:


```csharp
```

```csharp
var words = new string[]
{
                // index from start    index from end
    "The",      // 0                   ^9
    "quick",    // 1                   ^8
    "brown",    // 2                   ^7
    "fox",      // 3                   ^6
    "jumped",   // 4                   ^5
    "over",     // 5                   ^4
    "the",      // 6                   ^3
    "lazy",     // 7                   ^2
    "dog"       // 8                   ^1
};              // 9 (or words.Length) ^0
```

آرایه‌ی فوق، 9 عضو دارد. در این حالت اولین عنصر آن با ایندکس صفر قابل دسترسی است. در همین حالت همین ایندکس را اگر از آخر محاسبه کنیم، 9 خواهد بود و همینطور برای مابقی.
در حالت کلی ایندکس n^ معادل sequence.Length - n است. بنابراین sequence[^0] به معنای sequence[sequence.Length] است و هر دو مورد یک index out of range exception را صادر می‌کنند.

---

**معرفی نوع جدید Index**

در C# 8.0 زمانیکه می‌نویسم 1^، در حقیقت قطعه کد زیر را ایجاد کرده‌ایم:


```csharp
```

```csharp
var index = new Index(value: 1, fromEnd: true);
Index indexStruct = ^1;
var indexShortHand = ^1;
```

Index یک struct و نوع جدید در C# 8.0 می‌باشد که در فضای نام System قرار گرفته‌است. سه سطر فوق دقیقا به یک معنا هستند و هر کدام خلاصه شده و ساده شده‌ی سطر قبلی است.
در سطر اول، پارامتر fromEnd نیز قابل تعریف است. این fromEnd با مقدار true، همان عملگر ^ در اینجا است و عدم ذکر این عملگر به معنای false بودن آن است:


```csharp
```

```csharp
int[] a = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
Console.WriteLine(a[a.Length – 2]); // will write 8 on console.
Console.WriteLine(a[^2]); // will write 8 on console.

Index i5 = 5;
Console.WriteLine(a[i5]);        //will write 5 on console.

Index i2fromEnd = ^2;
Console.WriteLine(a[i2fromEnd]); // will write 8 on console.
```

در این مثال دو نمونه کاربرد fromEnd با مقدار false و سپس true را ملاحظه می‌کنید. در حالتیکه Index i5 = 5 تعریف شده‌است، دسترسی به عناصر آرایه همانند قبل از ایندکس صفر و از آغاز شروع می‌شود و نه از ایندکس یک.

---

یا می‌توان برای مثال توسط LINQ، از متدهای Skip و Take آن برای جدا کردن بازه‌ای از آرایه‌ی numbers استفاده کرد و یا حتی می‌توان از روش کپی کردن آرایه‌ها به آرایه‌ای جدید نیز کمک گرفت که در هر دو حالت، مراحلی که باید طی شوند قابل توجه است. با ارائه‌ی C# 8.0، این نوع دسترسی‌ها جزئی از قابلیت‌های زبان شده‌اند.


**روش دسترسی به بازه‌ای از اعضای یک آرایه در C# 8.0**

در C# 8.0 برای دسترسی به بازه‌ای از عناصر یک آرایه می‌توان از range expression که به صورت x..y نوشته می‌شود، استفاده کرد. در ادامه، مثال‌هایی را از کاربردهای عبارت .. ملاحظه می‌کنید:


```csharp
```

```csharp
var myArray = new string[] { "Item1", "Item2", "Item3", "Item4", "Item5" };
```

3..1 به معنای انتخاب بازه‌ای از المان 2 تا المان 3 است. در اینجا به واژه‌ی «المان» دقت کنید که معادل ایندکس آن در آرایه نیست. یعنی عدد ابتدای یک بازه دقیقا به ایندکس آن در آرایه اشاره می‌کند و عدد انتهای بازه، به ایندکس ماقبل آن (از این جهت که بتوان توسط 0^، انتهای بازه را مشخص کرد؛ بدون دریافت استثنای index out of range). به همین جهت به ابتدای بازه می‌گویند inclusive و به انتهای آن exclusive:


```csharp

---

**سؤال: زمانیکه بازه‌ای از یک آرایه را انتخاب می‌کنیم، آیا یک آرایه‌ی جدید ایجاد می‌شود، یا هنوز به همان آرایه‌ی قبلی اشاره می‌کند؟**

پاسخ: یک آرایه‌ی جدید ایجاد می‌شود؛ اما می‌توان با فراخوانی متد ()array.AsSpan پیش از انتخاب یک بازه، بازه‌ای را تولید کرد که دقیقا به همان آرایه‌ی اصلی اشاره می‌کند و یک کپی جدید نیست:


```csharp
```

```csharp
var arr = (new[] { 1, 4, 8, 11, 19, 31 }).AsSpan();
var range = arr[2..5];

ref int elt1 = ref range[1];
elt1 = -1;

int copiedElement = range[2];
copiedElement = -2;

Console.WriteLine($"range[1]: {range[1]}, range[2]: {range[2]}"); // output: range[1]: -1, range[2]: 19
Console.WriteLine($"arr[3]: {arr[3]}, arr[4]: {arr[4]}"); // output: arr[3]: -1, arr[4]: 19
```

در این مثال، آرایه‌ی اصلی را ابتدا تبدیل به یک Span کرده‌ایم و سپس بازه‌ای از روی آن انتخاب شده‌است. به همین جهت است که زمانیکه از [ref locals](https://www.dntips.ir/post/2610/c-7-ref-returns-and-ref-locals) برای تغییر عضوی از این بازه استفاده می‌شود، این تغییر بر روی آرایه‌ی اصلی نیز تاثیر می‌گذارد.
