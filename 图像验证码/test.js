//携程风控的js埋点
(function () {
    var siteId = '48a1de0bb769',url = '//webresource.c-ctrip.com/resaresonline/risk/ubtrms/latest/default/chlorofp.js?siteId=' + siteId, timeout = 10;
    var now = new Date();
    setTimeout(function () {
        var f = document.createElement('script');
        f.type = 'text/javascript';
        f.id = 'cfp__script';
        f.async = true;
        f.src = ('https:' == document.location.protocol ? 'https:' : 'http:') + url + "&v=" + now.getYear() + "-" +now.getMonth() + "-" + now.getDate();
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(f, s);
    }, timeout);
    window.cfp__startScriptLoad = 1 * new Date();
})();

//加载登陆方式
$(document).ready(function(){

    //校验身份证，卡号位数//$('#loginUid').bind('input propertychange', function() {

    $('#loginUid').blur( function() {
        var len = $("#loginUid").val().length ;
        var pwdlen = $("#loginPwd").val().length ;
        //var reg=/^[0-9]*$/;
        var reg = /(^\d{9}$)|(^\d{12}$)|(^\d{11}$)|(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
        var value =$("#loginUid").val();
        if(!reg.test(value)){
            $('#errors').show() ;
            $("#errors").html('<b></b>账户位数不对');
        }else if(len == 9 || len == 12 || len == 11  || len==15 || len == 18|| len == 0){
            $('#errors').hide() ;
        }else{
            error = ""
            $('#errors').show() ;
            $("#errors").html('<b></b>账户位数不对');
        }
    });
    //校验身//$('#loginPwd').bind('input propertychange', function() {

    $('#loginPwd').blur(function() {
        var value = $("#loginPwd").val() ;
        var pwdlen = $("#loginPwd").val().length ;
        var len = $("#loginUid").val().length ;
        var reg=/^[0-9]{6}/;
        var reg1=/^[0-9]*$/;
        var value1 =$("#loginUid").val();
        if(!reg1.test(value1)&&len<18){
            $('#errors').show() ;
            $("#errors").html('<b></b>账户位数不对');
        }else if(reg.test(value)||len==0 ||pwdlen==0){
            $('#errors').hide() ;
        }else{
            error = ""
            $('#errors').show() ;
            $("#errors").html('<b></b>密码位数不对');


        }
    });

    $('#errors').hide() ;
    $("#login_form ").validate({
        errorPlacement: function(error, element){
            $('#errors').show() ;
            //$("#errors").html('<b></b>'+error);
            $("#errors").html('<b></b>');
            error.appendTo($("#errors"));
        },
        rules: {

            loginPwd: {required : true,

            },

        },
        messages: {
            loginPwd:{required:"密码位数不对",},

        }
    });

    function encryptPwd(){
        var url=baseUrl+"/security/rest/getEncryptKey";
        var value = "";
        $.ajax({
            type: "post",
            url: url,
            dataType: "json",
            async:false,
            error: function() {
                $("#errors").html('<b></b>服务超时');
                $('#errors').show() ;
            },
            complete: function() {
                layer.closeAll('loading');
            },
            success:function(data) {
                value = data;
            }
        });
        return  value;
    }


    //顶象部分
    $('#btn').click(function () {
        var result = very.isSuccess();
        if (!result) {
            if (very.type=='DX'){
                $("#errors").html('<b></b>请完成验证');
            } else if (very.type=='IMG'){
                $("#errors").html('<b></b>验证码校验不通过');
            }

            $('#errors').show() ;
            return false;
        }else {

            $('#errors').hide() ;
        }


        // 登录部分
        var value = $("#loginPwd").val() ;
        var reg=/^[0-9]{6}/;
        var len = $("#loginUid").val().length ;

        //var reg1=/^[0-9]*$/;
        var reg1 = /(^\d{9}$)|(^\d{12}$)|(^\d{11}$)|(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
        var value1 =$("#loginUid").val();
        if(!reg1.test(value1) || !(len == 9 || len == 12 || len == 11  || len==15 || len == 18) ){
            $("#errors").html('<b></b>账户位数不对');
            $('#errors').show() ;
            return;
        }

        //按键登陆
        var data = encryptPwd();
        var pwd = $('#loginPwd').val();
        // 加密
        var encrypt = new JSEncrypt({default_key_size: 1024});
        encrypt.setPublicKey(data.publickKey);
        var pwd = encrypt.encrypt(pwd);
        var sKeyId =data.sKeyId;
        //携程风控的chloroToken
        var chloroToken;
        window.__cfpi = window.__cfpi || [];
        window.__cfpi.push(['_getChloroToken', function (result) {
            chloroToken = result
        }]);
        var submitUrl = baseUrl+'/login/member/submit' ;
        var obj = {
            backUrl      : backUrl,
            loginUid     : $('#loginUid').val(),
            loginPwd     : pwd,
            loginCaptcha : $('#loginCaptcha').val(),
            rememberPass : $('#rememberPass').val(),
            sKeyId:sKeyId,
            chloroToken:chloroToken ,
            token: very.token,
            channel: very.channel,
            language: very.language
        };



        if($("#login_form").valid()&&reg.test(value))
        {


            $.ajax({
                type: "post",
                url: submitUrl,
                data: obj,
                dataType: "json",
                async: true,
                /*error: function() {
                    $("#errors").html('<b></b>服务超时');
                    $('#errors').show() ;
                },*/

                beforeSend: function(){
                    layer.load(2, { //加载进度条
                        shade: [0.2,'#999999'] //0.1透明度的白色背景
                    });
                },
                complete: function () {
                    layer.closeAll('loading');
                },
                success: function (data) {
                    if (data.success) {
                        //用户行为跟踪
                        var trkObj = {events: "event11", eVar1: $("#loginUid").val()};
                        trk.trkObject(trkObj);
                        location.href = data.url;


                    } else {
                        console.log(data.message)
                        $("#errors").html('<b></b>' + data.message);
                        $('#errors').show();
                        $("#captcha div:first").remove();
                        getGtPicture();
                        if (data.code === 'credential') {

                            $("#errors").hide();
                            if (data.redirect) {
                                layer.confirm(data.message,{title:'提示', btn: ['确定']}, function(index){
                                    //do something
                                    location.href = baseUrl + data.url;
                                });

                            } else{
                                layer.alert(data.message,{title:'提示',area: '370px'})
                            }

                        } else {
                            if (data.redirect) {
                                location.href = baseUrl + data.url;
                            } else if (data.url == undefined) {
                                //captchaObj.reset();
                                //$("#captcha div:first").remove();
                                //getGtPicture();
                            } else {
                                $(".nc-login-content").load(baseUrl + data.url);
                            }
                        }
                    }
                }
            });

        }

       return false ;

    })
    // 获取顶象服务信息
    function getGtPicture(){
        very.refresh();
    }
});