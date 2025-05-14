# What is TxtGen?
## TxtGen is one of the simplist programs out there, a terminal program that generates a page such as this one:
(Copy and Paste into your browser)

    data:text/html,%3Cbody%20style%3D%22margin%3A0%3Bdisplay%3Aflex%3Bjustify-content%3Acenter%3Balign-items%3Acenter%3Bheight%3A100vh%3Bbackground-color%3Argb%2820%2C20%2C20%29%3B%22%3E%3Cdiv%20style%3D%22font-size%3A15vw%3Btext-align%3Acenter%3Bcolor%3A%23ffffff%3Bfont-family%3Arockwell%3B%22%3ETxtGen%3C%2Fdiv%3E%3C%2Fbody%3E
## From your own text and settings.
# It's basically just a glorified HTML preset.

# About TxtGen (In-Program Text)

**TxtGen is a small HTML utility I created due to a very specific problem: Sending people messages through links.**

I didn't want to have to resort to titling a random website something else every time since it's kind of cheap and you can't send long messages.
TxtGen may or may not solve this problem due to how your specific program handles URLs, but nevertheless it's a fun little utility that you can use as a screen billboard.

### How does TxtGen Work?
TxtGen works in a very simple manner: It takes a small, preset HTML string and inserts values into the parameters. After it's done doing that, it takes the HTML and runs it through a URL encoder, which turns `Hello World` into `Hello%20World`, something you've probably seen at the end of search engine URLs that contains your query. Then the program adds `data:text/html,` at the front of it, allowing your browser to display the HTML contained in the encoded URL.

The original program was made in under a day by **FractalScripts**.

---

**Tip:** If you want to save your generated page as a HTML file, you can paste the raw HTML into a text file and rename the file extension from `.txt` to `.html`. Alternatively you can also save it from your web browser with `[Ctrl + S]`.

**Tip 2:** Try using _"Inspect"_, _"View Code"_, or a similar tool in your web browser to tinker with the values and see them change in real time! You would need to know where the values are, but it shouldn't be too hard. After that you can come back and use `[enc]` to encode your modified HTML into a new link!

---

# How to download and use
(Unfortunately its Windows-only right now.)

Either download the `.zip` file and unzip it, or alternatively download the "Executable" folder and everything inside of it. After that you'll want to run `TxtGen.exe`. Windows SmartScreen might show a warning, and that's because it's unsigned software. You'll want to click on "More Info" and "Run anyway".

Please note that this is early development software and extremely basic, since I made it in my free time as a private utility to solve a tiny problem that didn't even end up getting really solved. This is a passion project and there is a big chance I will totally forget it and move on.

**Optional:** If you have python installed (In the start menu search "Python" and see if an app appears called "Python x.xx" or something similar.) you can download `TxtGen.py` from the "Source" folder and run that using Python. This is a better choice if you're just testing it out and you'll probably forget about it as it is lighter and doesn't bundle the whole of Python inside.
