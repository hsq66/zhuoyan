//code by jj(fx-zjjsg@163.com) @2013-12-08
var timer = '';
var delay = 5000;
$(function(){
	var nums = $(".banner_btn").length;
	$(".banner_btn").bind('mouseover',function(){
		play($(this).attr("num"),nums);
	});
	play(1,nums);
});
function play(num,nums){
	clearInterval(timer);
	num = num < 1 ? nums : num;
	num = num > nums ? 1 : num;

	$(".banner_btn").removeClass('current').eq(num-1).addClass('current');
	show(num);

	timer = setTimeout("play("+(++num)+","+nums+")",delay);
}
function show(num){
	$(".banner").css('display','none').stop().animate({'opacity':0},0).eq(num-1).css('display','').animate({'opacity':1},500);
}