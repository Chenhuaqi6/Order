;
function SmoothlyMenu() {
    if (!$('body').hasClass('mini-navbar') || $('body').hasClass('body-small')) {
        // Hide menu in order to smoothly turn on when maximize menu
        $('#side-menu').hide();
        // For smoothly turn on menu
        setTimeout(
            function () {
                $('#side-menu').fadeIn(400);
            }, 200);
    } else if ($('body').hasClass('fixed-sidebar')) {
        $('#side-menu').hide();
        setTimeout(
            function () {
                $('#side-menu').fadeIn(400);
            }, 100);
    } else {
        // Remove all inline style from jquery fadeIn function to reset menu state
        $('#side-menu').removeAttr('style');
    }
}

// Full height of sidebar
function fix_height() {
    var heightWithoutNavbar = $("body > #wrapper").height() - 61;
    $(".sidebard-panel").css("min-height", heightWithoutNavbar + "px");

    var navbarHeigh = $('nav.navbar-default').height();
    var wrapperHeigh = $('#page-wrapper').height();

    if (navbarHeigh > wrapperHeigh) {
        $('#page-wrapper').css("min-height", navbarHeigh + "px");
    }

    if (navbarHeigh < wrapperHeigh) {
        $('#page-wrapper').css("min-height", $(window).height() + "px");
    }

    if ($('body').hasClass('fixed-nav')) {
        if (navbarHeigh > wrapperHeigh) {
            $('#page-wrapper').css("min-height", navbarHeigh - 60 + "px");
        } else {
            $('#page-wrapper').css("min-height", $(window).height() - 60 + "px");
        }
    }

}

var common_ops = {
    init:function(){
        this.eventBind();
        this.setMenuIconHighLight();
    },
    eventBind:function(){
        $('.navbar-minimalize').click(function () {
            $("body").toggleClass("mini-navbar");
            SmoothlyMenu();
        });

        $(window).bind("load resize scroll", function () {
            if (!$("body").hasClass('body-small')) {
                fix_height();
            }
        });
    },
    setMenuIconHighLight:function(){
         if( $("#side-menu li").size() < 1 ){
            return;
        }

        var pathname = window.location.pathname;
        var nav_name = "default";


        if(  pathname.indexOf("/account") > -1  ){
            nav_name = "account";
        }


        if(  pathname.indexOf("/food") > -1  ){
            nav_name = "food";
        }

        if(  pathname.indexOf("/member") > -1  ){
            nav_name = "member";
        }

        if(  pathname.indexOf("/finance") > -1  ){
            nav_name = "finance";
        }

        if(  pathname.indexOf("/qrcode") > -1  ){
            nav_name = "market";
        }

        if(  pathname.indexOf("/stat") > -1  ){
            nav_name = "stat";
        }

        if( nav_name == null ){
            return;
        }

        $("#side-menu li."+nav_name).addClass("active");
    },
    alert:function( msg ,cb ){
        layer.alert( msg,{
            yes:function( index ){
                if( typeof cb == "function" ){
                    cb();
                }
                layer.close( index );
            }
        });
    },
    confirm:function( msg,callback ){
        callback = ( callback != undefined )?callback: { 'ok':null, 'cancel':null };
        layer.confirm( msg , {
            btn: ['确定','取消'] //按钮
        }, function( index ){
            //确定事件
            if( typeof callback.ok == "function" ){
                callback.ok();
            }
            layer.close( index );
        }, function( index ){
            //取消事件
            if( typeof callback.cancel == "function" ){
                callback.cancel();
            }
            layer.close( index );
        });
    },
    tip:function( msg,target ){
        layer.tips( msg, target, {
            tips: [ 3, '#e5004f']
        });
        $('html, body').animate({
            scrollTop: target.offset().top - 10
        }, 100);
    },
    buildUrl:function( path ,params ){
        var url = "" + path;
        var _paramUrl = "";
        if(  params ){
            _paramUrl = Object.keys( params ).map( function( k ){
                return [ encodeURIComponent( k ),encodeURIComponent(params[k])].join("=");
            }).join("&");
            _paramUrl = "?" + _paramUrl;
        }
        return url + _paramUrl;
    },
    buildPicUrl:function (img_key) {
        var domain = $(".hidden_layout_wrap input[name=domain]").val()
        var prefix_url = $(".hidden_layout_wrap input[name=prefix_url]").val()
        return domain+prefix_url+img_key
    }

};

$(document).ready( function() {
    common_ops.init();
});

