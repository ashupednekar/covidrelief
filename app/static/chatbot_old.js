var app = {
    appURL: 'https://nbf.bankbuddy.ai/webchat/',
    chatIcon: 'logo.png',
    chatLogo: 'logo.png',
    appHead: 'nbf',
    appDesc: 'Leading Excellence',
    apphideHead: '.b-agent-demo_header',
}
var themeColor = {
    HeaderbgColor: '#1d469e',
    chatBg: '#fff',
    borderColor: '1px solid #cecece'
}
//icon => i
//Header => h
//extra info =>e
function chatBox(_item, _theme) {
    this._item = _item;
    this._theme = _theme;
}

function chatToggle(_this, chatDiv) {
    $(_this).hide();
    $(chatDiv).show();
}
chatBox.prototype.createDom = function() {
    var styleTag = document.createElement('style');
    var div = document.createElement("div");
    var main_div = $(div).attr('id', 'ico');
    var _img = document.createElement('img');
    _img.setAttribute('src', this._item.chatIcon);
    $('body').append(main_div);
    $('head').append('<link href="chatstyle.css" rel="stylesheet" />');
    $(main_div).append(_img);
    $('body').append('<div id="main-chat-wrapper" style="background:' + this._theme.chatBg + ';border:' + this._theme.borderColor + ';z-index:10000"></div>');
    $('#main-chat-wrapper').append('<header class="chat-header"></header>');
    $('.chat-header').append('<div class="header-wrapper"><a class="close"><i class="fa fa-times" style="color:white"></i></a></div>');
    var url = this._item.appURL;

    $('#main-chat-wrapper').find('iframe').remove();
    $('#main-chat-wrapper').append('');
    //$('#content').removeAttr('src');[iframe id="content" src="' + url + '"]

    $('#ico').click(function() {
        chatToggle($(this), '#main-chat-wrapper');
        /*if($('#main-chat-wrapper').find('iframe')){
                 }*/

        /*setTimeout(function(){
         var iframe = document.getElementById('content');
          var ele = iframe.contentWindow.document.getElementsByClassName('b-agent-demo_header')[0];
          ele.style.display = 'none';
        },1000)*/
    });
    // $("#content").contents().find(".b-agent-demo_header").remove();
    $('.close').click(function() {
        chatToggle('#main-chat-wrapper', '#ico');
    });
}

var demo = new chatBox(app, themeColor);

demo.createDom();
