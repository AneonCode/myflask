$(function() {
    $("#ido").fullpage(
        {
            loopBottom: true,
            navigation: true,
            easingcss3: 'cubic-bezier(0.175, 0.885, 0.320, 1.275)'

        }
    );
});

$(function () {
    $(".pic-div").css({
        'height': $(".pic-div").width()
    })
});

$(function () {
    $("#pic1-div, #pic11-div, #pic21-div, #pic31-div, #pic41-div, #pic51-div, #pic61-div").css({
        'left': '25%',
        'top': '20%'
    })
});
$(function () {
    $("#pic2-div, #pic12-div, #pic22-div, #pic32-div, #pic42-div, #pic52-div, #pic62-div").css({
        'left': document.getElementById($("#pic1-div, #pic11-div, #pic21-div, #pic31-div, #pic41-div, #pic51-div, #pic61-div").attr("id")).getBoundingClientRect().left + (document.getElementById($("#pic1-div, #pic11-div, #pic21-div, #pic31-div, #pic41-div, #pic51-div, #pic61-div").attr("id")).getBoundingClientRect().width)/2,
        'top': document.getElementById($("#pic1-div, #pic11-div, #pic21-div, #pic31-div, #pic41-div, #pic51-div, #pic61-div").attr("id")).getBoundingClientRect().top + (document.getElementById($("#pic1-div, #pic11-div, #pic21-div, #pic31-div, #pic41-div, #pic51-div, #pic61-div").attr("id")).getBoundingClientRect().width)/2,
    });
    $("#pic3-div, #pic13-div, #pic23-div, #pic33-div, #pic43-div, #pic53-div, #pic63-div").css({
        'left': document.getElementById($("#pic2-div, #pic12-div, #pic22-div, #pic32-div, #pic42-div, #pic52-div, #pic62-div").attr("id")).getBoundingClientRect().left + (document.getElementById($("#pic2-div, #pic12-div, #pic22-div, #pic32-div, #pic42-div, #pic52-div, #pic62-div").attr("id")).getBoundingClientRect().width)/2,
        'top': document.getElementById($("#pic1-div, #pic11-div, #pic21-div, #pic31-div, #pic41-div, #pic51-div, #pic61-div").attr("id")).getBoundingClientRect().top,
    });
    $("#pic4-div, #pic14-div, #pic24-div, #pic34-div, #pic44-div, #pic54-div, #pic64-div").css({
        'left': document.getElementById($("#pic3-div, #pic13-div, #pic23-div, #pic33-div, #pic43-div, #pic53-div, #pic63-div").attr("id")).getBoundingClientRect().left + (document.getElementById($("#pic3-div, #pic13-div, #pic23-div, #pic33-div, #pic43-div, #pic53-div, #pic63-div").attr("id")).getBoundingClientRect().width)/2,
        'top': document.getElementById($("#pic2-div, #pic12-div, #pic22-div, #pic32-div, #pic42-div, #pic52-div, #pic62-div").attr("id")).getBoundingClientRect().top,
    });
    $("#pic5-div, #pic15-div, #pic25-div, #pic35-div, #pic45-div, #pic55-div, #pic65-div").css({
        'left': document.getElementById($("#pic4-div, #pic14-div, #pic24-div, #pic34-div, #pic44-div, #pic54-div, #pic64-div").attr("id")).getBoundingClientRect().left + (document.getElementById($("#pic4-div, #pic14-div, #pic24-div, #pic34-div, #pic44-div, #pic54-div, #pic64-div").attr("id")).getBoundingClientRect().width)/2,
        'top': document.getElementById($("#pic1-div, #pic11-div, #pic21-div, #pic31-div, #pic41-div, #pic51-div, #pic61-div").attr("id")).getBoundingClientRect().top,
    })
});
$(function () {
    $(".pic-reponsive").css({
        'height': document.getElementById($("#pic1-div").attr("id")).getBoundingClientRect().height,
        'width': 'auto'
    })
});
$(function () {
    $(".pic-div").hover(function () {
	
        $(".pic-div").css({
            opacity: 0.4
        });
        $(this).css({
            opacity: 1
        });
            $(this).find(".dask").stop().delay(50).animate({
                opacity: 0.8
            },300);
            $(this).css({
                'clip-path': 'polygon(0 0, 100% 0, 100% 100%, 0 100%)'
            });
            $(this).find(".dask").css({
                'clip-path': 'polygon(0 0, 100% 0, 100% 100%, 0 100%)'
            });
        },
        function () {
	 
            $(".pic-div").css({
                opacity: 1
            });
            $(".dask").stop().animate({
                opacity:0
            },300);
            $(this).css({
                'clip-path': 'polygon(50% 0, 100% 50%, 50% 100%, 0 50%)'
            });
            $(this).find(".dask").css({
                'clip-path': 'polygon(50% 0, 100% 50%, 50% 100%, 0 50%)'
            })
        })
});
$(function () {
    $(".dask").css({
        'height': $(".dask").width()
    })
});