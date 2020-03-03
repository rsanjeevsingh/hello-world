# hello-world
my first repository
Edited in branch-1
Sub test()

    Dim ie As New InternetExplorer
    Dim hDoc As MSHTML.HTMLDocument
    Dim hElmt As MSHTML.IHTMLElement
    Dim hElmts As MSHTML.IHTMLElementCollection
    Dim X, LR, i As Long
    Dim A1, A2 As Long


    
    ie.navigate "http://nseindia.com/option-chain"
    
    ie.Visible = False
    
    Application.Wait (Now + TimeValue("0:00:10"))
        
    Set hDoc = ie.document
    
    Set htable = hDoc.getElementById("optionChainTable-indices")
    i = 1
    j = 1
    For Each hElmt In htable.getElementsByTagName("tr")
        For Each hele In hElmt.getElementsByTagName("td")
            Sheet1.Cells(i, j) = hele.innerText
            j = j + 1
        Next hele
        j = 1
        i = i + 1
    Next hElmt
    
    Set ie = Nothing
End Sub
