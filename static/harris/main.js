$(document).ready(function() {
   $('.card').each(function(_, obj) {
        let primary = $(obj).attr("color1");
        let secondary = $(obj).attr("color2");
        let text = $(obj).attr("text-color");
        let angle = $(obj).attr("angle") || 0;
        $(obj).attr("style", "color:"+text+"; background: linear-gradient("+angle+","+primary+", "+secondary);
    });
});