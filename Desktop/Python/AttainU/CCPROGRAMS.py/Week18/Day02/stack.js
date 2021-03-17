let data = []
var push = document.getElementById("push");
var pop = document.getElementById("pop");
var ans = document.getElementById("ans");
push.addEventListener("click",function(){
    var texts = document.getElementById("texts");
    data.push(texts.value);
    ans.innerHTML= data;
    texts.value = "";
});

pop.addEventListener("click",function(){
    data.pop();
    ans.innerHTML= data;
});
