# ABOUT TXTGEN

**TxtGen is a small HTML utility I created due to a very specific problem: Sending people messages through links.**

I didn't want to have to resort to titling a random website something else every time since it's kind of cheap and you can't send long messages.
TxtGen may or may not solve this problem due to how your specific program handles URLs, but nevertheless it's a fun little utility that you can use as a screen billboard.

### How does TxtGen Work?
TxtGen works in a very simple manner: It takes a small, preset HTML string and inserts values into the parameters. After it's done doing that, it takes the HTML and runs it through a URL encoder, which turns `Hello World` into `Hello%20World`, something you've probably seen at the end of search engine URLs that contains your query. Then the program adds `data:text/html,` at the front of it, allowing your browser to display the HTML contained in the encoded URL.

The original program was made in under a day by **FractalScripts**.

---

**Tip:** If you want to save your generated page as a HTML file, you can paste the raw HTML into a text file and rename the file extension from `.txt` to `.html`. Alternatively you can also save it from your web browser with `[Ctrl + S]`.

**Tip 2:** Try using _"Inspect"_, _"View Code"_, or a similar tool in your web browser to tinker with the values and see them change in real time! You would need to know where the values are, but it shouldn't be too hard. After that you can come back and use `[enc]` to encode your modified HTML into a new link!
