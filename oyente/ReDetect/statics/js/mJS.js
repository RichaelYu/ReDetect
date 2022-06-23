// 当点某一个标签的时候对应的 div 显示，其他的隐藏。
// 查找触发事件的元素
var as = document.querySelectorAll("#tab a");
// 绑定事件处理函数
for (var i = 0; i < as.length; i++) {
    as[i].onclick = function () {
        // 隐藏所有的 div
        var divs = document.querySelectorAll("#content>div");
        for (var i = 0; i < divs.length; i++) {
            divs[i].style.display = "none";
        }
        // 让对应的 div显示
        // 获取当前的 a 的 href
        var i = this.href.lastIndexOf("#");
        var id = this.href.slice(i);
        console.log(id)
        document.querySelector(id).style.display = "block";
    }
 
}