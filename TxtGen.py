import urllib.parse
import html
import time

def gen():
    global text, size, color, bgcolor, font, height, margin

    text=""
    size="10"
    color="#ffffff"
    bgcolor="#000000"
    font="sans-serif"

    height="100"
    margin="0"

    print("")
    print("")
    print("")
    print("Input Text: (Special characters will be automatically encoded)")
    txtin=True
    textbuffer=""
    textbuffer=textbuffer+html.escape(input())
    print("===# Press [ENTER] to finalize text | Input anything else and hit [ENTER] to make a new line #===")
    if input()=="":
        txtin=False
    else:
        txtin=True
    while txtin:
        time.sleep(1)
        textbuffer=textbuffer+"<br>"+html.escape(input())
        print("=# Finalize:[ENTER] | Newline:ANY+[ENTER] #=")
        if input()=="":
             txtin=False
    text=textbuffer
    print("")
    print("Text finalized")
    print("")
    print("")
    print("")
    print("===# Press [ENTER] to generate with default parameters | Input anything else and hit [ENTER] to adjust parameters #===")
    if input()=="":
        print("")
        print("")
        print("")
        print("=====HTML=====")
        print(genenc(True))
        print("=====HTML=====")
        print("")
        print("=====LINK=====")
        print("data:text/html,"+genenc(False))
        print("=====LINK=====")
        print("")
        print("Press [ENTER] to reset")
        input()
        main()
    else:
        print("")
        print("")
        print("")

        print("Text Size: (Numbers only, or the HTML will be broken) = Default is [10]")
        size=input()

        print("Text Color: (Either HEX value [#ffffff] or RGB [rgb(255, 255, 255)]) = Default is [#ffffff]")
        color=input()

        print("Background Color: (Either HEX value [#000000] or RGB [rgb(0, 0, 0)]) = Default is [#000000]")
        bgcolor=input()

        print("Font: (Must be web safe) = Default is [sans-serif]")
        font=input()
        
        print("")
        print("")
        print("")
        print("===# Press [ENTER] to generate now | Input anything else and hit [ENTER] to adjust advanced parameters (They do little to nothing) #===")

        if input()=="":
            print("")
            print("")
            print("")
            print("=====HTML=====")
            print(genenc(True))
            print("=====HTML=====")
            print("")
            print("=====LINK=====")
            print("data:text/html,"+genenc(False))
            print("=====LINK=====")
            print("")
            print("Press [ENTER] to reset")
            input()
            main()
        else:
            print("")
            print("")
            print("")

            print("Height: (Numbers only, or the HTML will be broken) = Default is [100]")
            height=input()

            print("Margin: (Numbers only, or the HTML will be broken) = Default is [0]")
            margin=input()

            print("")
            print("")
            print("")
            print("===# Press [ENTER] to generate #===")

            print("")
            print("")
            print("")
            print("=====HTML=====")
            print(genenc(True))
            print("=====HTML=====")
            print("")
            print("=====LINK=====")
            print("data:text/html,"+genenc(False))
            print("=====LINK=====")
            print("")
            print("Press [ENTER] to reset")
            input()
            main()

def genenc(htmlreturn):
    txthtml="<body style=\"margin:"+margin+";display:flex;justify-content:center;align-items:center;height:"+height+"vh;background-color:"+bgcolor+";\"><div style=\"font-size:"+size+"vw;text-align:center;color:"+color+";font-family:"+font+";\">"+text+"</div></body>"

    txtenc=urllib.parse.quote(txthtml, safe='')

    if htmlreturn:
        return(txthtml)
    else:
        return(txtenc)

def enc():
    print("")
    print("")
    print("")
    print("Insert HTML to be URL encoded:")
    encval=input()
    encout=urllib.parse.quote(encval, safe='')
    encfullout="data:text/html,"+encout
    print("=====URL ENCODED=====")
    print(encout)
    print("=====URL ENCODED=====")
    print("")
    print("=====VIEWABLE LINK=====")
    print(encfullout)
    print("=====VIEWABLE LINK=====")
    print("")
    print("Press [ENTER] to reset")
    input()
    main()

def abt(namesub):
    print("")
    print("")
    print("")
    print("ABOUT TXTGEN")
    print("===============")
    print("TxtGen is a small HTML utility I created due to a very specific problem: Sending people messages through links.")
    print("")
    print("I didn't want to have to resort to titling a random website something else every time since it's kind of cheap and you can't send long messages.")
    print("TxtGen may or may not solve this problem due to how your specific program handles URLs, but nevertheless it's a fun little utility that you can use as a screen billboard.")
    print("")
    print("How does TxtGen Work?")
    print("TxtGen works in a very simple manner: It takes a small, preset HTML string and inserts values into the parameters. After it's done doing that, it takes the HTML and runs it through a URL encoder, which turns \"Hello World\" into \"Hello%20World\", something you've probably seen at the end of search engine URLs that contains your query. Then the program adds \"data:text/html,\" at the front of it, allowing your browser to display the HTML contained in the encoded URL.")
    print("")
    print("This program was made in under a day by "+namesub+".")
    print("")
    print("Tip: If you want to save your generated page as a HTML file, you can paste the raw HTML into a text file and rename the file extension from \".txt\" to \".html\". Alternatively you can also save it from your web browser with [Ctrl + S].")
    print("")
    print("Tip 2: Try using \"Inspect\", \"View Code\", or a similar tool in your web browser to tinker with the values and see them change in real time! You would need to know where the values are, but it shouldn't be too hard. After that you can come back and use [enc] to encode your modified HTML into a new link!")
    print("")
    print("Press [ENTER] to reset")
    input()
    main()

def main():
    name="FractalScripts"
    print(" _____      _    ____            ")
    print("|_   _|_  _| |_ / ___| ___ _ __  ")
    print("  | | \\ \\/ / __| |  _ / _ \\ '_ \\ ")
    print("  | |  >  <| |_| |_| |  __/ | | |")
    print("  |_| /_/\\_\\\\__|\\____|\\___|_| |_|")
    print("=================================")
    print("")
    print("TXTGEN UTILITY")
    print("Made by "+name)
    print("")
    print("Type [gen] to generate a text page | Type [enc] to encode an already existing HTML | Type [abt] to read about this program")

    inval=input()
    if inval=="gen":
        gen()
    elif inval=="enc":
        enc()
    elif inval=="abt":
        abt(name)

main()