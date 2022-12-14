# Week6 : Regex and Web crawling


⚪️ Lesson:<br>
&emsp;&ensp;1- Regex  
&emsp;&ensp;2- web crawling <br>

⚪️ Tools:<br>
&emsp;&ensp;1- Beautiful-soup  
&emsp;&ensp;2- Scrapy 

⚪️ For next week:
        <br>&emsp;&ensp;1- Crawl tsetmc.com 
        <br>&emsp;&ensp;2- Crawl Jabinja
        

⚪️ What I did:
        <br>&emsp;&ensp;1- Crawl tsetmc.com 
        <br>&emsp;&ensp;دو جدول از این سایت کرال شد باقی جداول شبیه به همین دو جدول است
        <br>&emsp;&ensp;تگ هایی که باید برای کرال تشخیص داد از صفحه view page source هم بهتر است چک شود نه فقط صفحه Inspect
        <br>&emsp;&ensp;در مورد تگ ها نکته مهم این است که وقتی یک تگ سلکت می شود همه تگ های مشابه که ذیل این تگ باشند انتخاب می شود و با شماره می توان ترتیب آن ها را تشخیص داد
        <br>&emsp;&ensp;از عمگلر یا می توان در تعریف  رشته داخلی سلکتور استفاده کرد
        <br>&emsp;&ensp;برای هر جدول یک اسپایدر در نظر گرفته شد
        <br>&emsp;&ensp;دستور اجرای اسپایدر و انتقال دیتا به فایل:
        <br>&emsp;&ensp;scrapy crawl Table1 -o table1.csv
        <br>&emsp;&ensp;Table1 نام اسپایدر و -o یعنی به فایل اپند شود اگز -O بگذاریم فایل جدید ایجاد می شود
