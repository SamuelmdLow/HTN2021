var ADD_BAR = document.createElement("DIV");
ADD_BAR.setAttribute("onmouseenter", "button(this)");
ADD_BAR.setAttribute("onmouseleave", "setTimeout(removeButtons, 250, this)");
ADD_BAR.setAttribute("style", "margin:1%;");

var ADD = document.createElement("DIV");
ADD.setAttribute("class", "addNew");
ADD.innerHTML = "Add";

ADD_BAR.appendChild(ADD);


function insertSection(button, elem)
{
    const content = document.getElementById("content");
    index = Array.prototype.indexOf.call(content.children, button.parentElement.parentElement)
    content.insertBefore(elem, content.children[index]);
}

function removeButtons(elem)
{
    while (elem.children.length > 0) {
        elem.removeChild(elem.children[0]);
    }

    var ADD = document.createElement("DIV");
    ADD.setAttribute("class", "addNew");
    ADD.innerHTML = "ADD";
    elem.appendChild(ADD);
}

function buttons(elem)
{
    while (elem.children.length > 0) {
        elem.removeChild(elem.children[0]);
    }

    var CH = document.createElement("DIV");
    CH.setAttribute("class", "addNew");
    CH.setAttribute("onclick", "insertSection(this,newChapter())");
    CH.innerHTML = "CH";

    var TXT = document.createElement("DIV");
    TXT.setAttribute("class", "addNew");
    TXT.setAttribute("onclick", "insertSection(this,newText())");
    TXT.innerHTML = "TXT";

    var DEF = document.createElement("DIV");
    DEF.setAttribute("class", "addNew");
    DEF.setAttribute("onclick", "insertSection(this,newDefinition())");
    DEF.innerHTML = "DEF";

    elem.appendChild(CH);
    elem.appendChild(TXT);
    elem.appendChild(DEF);
}

function newChapter()
{
    var div = document.createElement("SECTION");
    div.setAttribute("class", "CH");

    var input = document.createElement("INPUT");
    input.setAttribute("type", "text");
    input.setAttribute("class", "editChapter");

    div.appendChild(ADD_BAR);
    div.appendChild(input)

    return div;
}

function newText()
{
    var div = document.createElement("SECTION");
    div.setAttribute("class", "TXT");

    var input = document.createElement("INPUT");
    input.setAttribute("type", "text");
    input.setAttribute("class", "editText");

    div.appendChild(ADD_BAR);
    div.appendChild(input)

    return div;
}

function newDefinition()
{
    var div = document.createElement("SECTION");
    div.setAttribute("class", "DEF");

    var input1 = document.createElement("INPUT");
    input1.setAttribute("type", "text");
    input1.setAttribute("class", "editDef");



    var input2 = document.createElement("INPUT");
    input2.setAttribute("type", "text");
    input2.setAttribute("class", "editText");

    div.appendChild(ADD_BAR);
    div.appendChild(input1)
    div.appendChild(input2)

    return div;
}

function update()
{
    var s = "";
    var content = document.getElementById("content").children;

    for (let a = 0; a < content.length; a++)
    {
        if (content[a].tagName == "SECTION")
        {
            s = s + "|" + content[a].className;
            elems = content[a].children;
            for (let b = 0; b < elems.length; b++)
            {
                if (typeof elems[b].value != "undefined")
                {
                    s = s + "," + elems[b].value;
                }
            }
        }
    }

    document.getElementById("contents").value = s;
    document.getElementById("info").submit();
}
