import re

#https://www.ichunqiu.com/courses

html = '''

<!DOCTYPE html>
<html>
<head>
	<title>【网络安全_信息安全_白帽子】_知识体系_教程_培训_在线实验_i春秋</title>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="description" content="i春秋（www.ichunqiu.com）专注网络安全、信息安全、白帽子技术的在线学习，教育、培训的平台。知识体系频道为网络安全、信息安全、白帽子技术爱好者提供便捷,优质的视频教程和实验室环境，教程涵盖Web安全、漏洞分析、Android安全、iOS安全、企业安全等权威专业视频教程.">
	<meta name="keywords" content="网络安全,信息安全,白帽子,网络安全知识培训,在线实验,信息安全知识">
<!-- icon -->
<link rel="shortcut icon" href="https://static2.ichunqiu.com/icq/resources/images/favicon.ico">
<link rel="stylesheet" href="https://static2.ichunqiu.com/icq/resources/css/courses/courses.css?v=1971d4d709a8ff4b8adf2d40019bfc08" type="text/css" media="screen">
</head>
<body>
	<!-- 插件css -->
<link rel="stylesheet" type="text/css" href="https://static2.ichunqiu.com/icq/resources/css/plugin/bootstrap.min.css?v=4cd0c71d98" />
<link rel="stylesheet" type="text/css" href="https://static2.ichunqiu.com/icq/resources/css/plugin/jquery.mCustomScrollbar.min.css" />
<!-- 公共css -->
<link rel="stylesheet" type="text/css" href="https://static2.ichunqiu.com/icq/resources/css/common/component.css?v=e9d8sas5"/>
<!-- 头部css -->
<link rel="stylesheet" type="text/css" href="https://static2.ichunqiu.com/icq/resources/css/common/header.css?v=c02f8e8b4c"/>
<!--企安殿4.0新用户登陆css-->
<link rel="stylesheet" type="text/css" href="https://static2.ichunqiu.com/icq/resources/css/company/qad/qadfyd.css"/>
<!--用户体系小I-->
<link rel="stylesheet" type="text/css" href="https://static2.ichunqiu.com/icq/resources/css/IRD/IRD-i.css?v=bb644b03ae5da915505e3f6da2d08d46"/>
<link rel="stylesheet" type="text/css" href="https://static2.ichunqiu.com/icq/resources/css/IRD/robot.css?v=bb644b03ae5da915505e3f6da2d08d46"/>
<!--[if IE 8]>
<style>
/*ie8可圆角*/
	.css3PIE{
		position: relative;
		z-index: 2;
		behavior: url('https://static2.ichunqiu.com/icq/resources/css/plugin/css3PIE.htc');
	}
</style>
<![endif]-->
<style>
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('https://www.ichunqiu.com/resources/fonts/glyphicons-halflings-regular.eot');
  src: url('https://www.ichunqiu.com/resources/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('https://www.ichunqiu.com/resources/fonts/glyphicons-halflings-regular.woff') format('woff'), url('https://www.ichunqiu.com/resources/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('https://www.ichunqiu.com/resources/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
</style>
<!--企安殿4.0新入口引导-->		
<div class="new_rktk"></div>
<div class="new_rk">
	<div class="sd"></div>
	<div class="new_text">
		<span></span>
		<button>我知道了</button>
	</div>
</div>

<!--检测用户是否禁用cookie-->
<div class="checkIsCookie">
    <p>未开启cookie无法登录使用i春秋的完整服务，请设置开启浏览器cookie</p>
    <a href="javascript:;" class="checkIsCookieClose"></a>
</div>

<!-- 头部html -->
<div class="header">
 	<img id="wx_global_pic" src="https://static2.ichunqiu.com/icq/resources/images/common/logo400slogan.jpg" style="position:absolute;z-index:0;left: -10000px;">
	<div class="login">
		<div class="colororange">
							<a class="logo" href="https://www.ichunqiu.com/"></a>
				
						
			<div class="mainSrh">
				<input id="searchVal" type="text" placeholder="搜索课程、竞赛或讲师">
				<a id="searchIcon" target="_blank" href="javascript:void(0)">
					<i class="ficon search"></i>
				</a>
			</div>
			<div class="hotsear"></div>
			<div class="loginright">
				<div class="apppys pxzhujiao"></div>
				<div class="apppys qiandian"></div>
				<div class="apppys">
					<i class="ficon phone"></i>
					<a href="https://www.ichunqiu.com/default/apppys">下载App</a>
					<img class="android" src="https://static2.ichunqiu.com/icq/resources/images/common/androidapp.png" alt="Android">
				</div>

				<!-- 登陆后 -->
									<!-- 登陆前/暂时页面隐藏 -->
					<div class="loginbefore" style="display:inline-block;">
						<a href="https://user.ichunqiu.com/login" id="setstorage" rel="nofollow">登录</a>
						<span>丨</span>
						<a href="https://user.ichunqiu.com/register/" rel="nofollow">注册</a>
											</div>
							</div>
		</div>
	</div>
	<div id="hidiv" style="display: none;"></div>
	<div class="headernav">
		<ul>
			<li data-val="0"><a style="padding-left: 0px;" href="https://www.ichunqiu.com/">首页</a></li>
			<li data-val="1"><a href="https://www.ichunqiu.com/courses">知识体系</a></li>
			<li data-val="2"><a href="https://www.ichunqiu.com/#profession">职业成长</a></li>
			<li data-val="3"><a href="https://www.ichunqiu.com/competition">CTF大本营</a></li>
			<li data-val="9"><a class="newnav listHot" href="https://www.ichunqiu.com/train">培训认证</a></li>
			<li data-val="4"><a href="https://www.ichunqiu.com/default/qiand">企安殿</a></li>
			<li data-val="10"><a class="newnav" href="https://www.ichunqiu.com/safety">安全意识</a></li>
			<li data-val="11"><a href="https://www.ichunqiu.com/xuetang">春秋学堂</a></li>
			<li data-val="8"><a href="https://www.ichunqiu.com/src">SRC部落</a></li>
			<!--<li data-val="5"><a href="https://www.ichunqiu.com/opencourse">公开课</a></li>
			<li data-val="6"><a href="https://www.ichunqiu.com/recruit">讲师招募</a></li>-->
			<li data-val="7"><a target="_blank" href="https://bbs.ichunqiu.com/?from=xueyuan" id="bd_bbs_tj">社区</a></li>
            <li data-val="13"><a href="http://culture.ichunqiu.com/" target="_blank">春秋游戏</a></li>
			<li data-val="12" name="right"><a target="_blank" href="https://www.ichunqiu.com/member/index" data-svg="yenjoy">优享会员</a></li>
		</ul>
	</div>
	<div class="right-nav-box">
		<!--双11新增浮框-->
		<div class="right-nav double11" style="display: none;" onclick="window.location.href='https://www.ichunqiu.com/active2017/Topic/index'">
			<div class="kfpic"><img src="https://static2.ichunqiu.com/icq/resources/images/double11/hovershow11.jpg"></div>
		</div>
		<!--CTF大本营我要办比赛页面专属-->
		<div class="right-nav ctf" style="display: none;" scrollto=".callus" scrollheight="40">		
		</div>
		<div class="right-nav kf">
			<div class="kfpic"></div>
		</div>
		<div class="right-nav qq">
			<a href="tencent://message/?uin=2097706690&Site=i春秋&Menu=yes"></a>
		</div>
		<div class="right-nav app">
			<div class="apppic"></div>
		</div>

		<div class="right-nav wx">
			<div class="wxpic"></div>
		</div>
		<div class="right-nav wb">
			<div class="wbpic"></div>
		</div>
		<div class="right-nav totop"></div>
	</div>
</div>
			<!--双11新增小banner-->
					
		<div class="coursesMain">
			<div class="coursesType">
				<div class="typeTitle">
					<h1>知识体系</h1>
				</div>
				<div class="direction orientation">
					<div class="leftPart">
						<span class="tag">方向：</span>
						<span class="lab all active">
                                                                                                <a href="https://www.ichunqiu.com/courses">全部</a>
                                                            						</span>
					</div>
					<div class="typeList">
													                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/mqtaq" labelId="244"> 名企谈安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/qyaq" labelId="313"> 企业安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/wzaq" labelId="246"> 网站安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/khdaq" labelId="247"> 客户端安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/txaq" labelId="248"> 通信安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/ydaq" labelId="249"> 移动安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/znyjaq" labelId="250"> 智能硬件安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/gkaq" labelId="251"> 工控安全</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/aqll" labelId="252"> 安全理论</a>
                                                                                                    </span>
							                                <span class="lab ">
                                <!--<a href="--><!--">--><!--</a>-->
                                                                                                            <a href="https://www.ichunqiu.com/courses/ctf" labelId="393"> CTF学习</a>
                                                                                                    </span>
																		</div>
				</div>
				<div class="classify">
					<div class="leftPart">
						<span class="tag">分类：</span>
						<span class="lab all active">
                                                                                                                                        <a href="https://www.ichunqiu.com/courses">全部</a>
                                                                                                <!--							<a href="--><!--">全部</a>-->
						</span>
					</div>
					<div class="typeList add_type">
													                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/qmxc" labelId="253">启明星辰</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/zdcy" labelId="254">知道创宇 </a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/qh360" labelId="255">奇虎360 </a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/jnta" labelId="256">江南天安</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/wkaq" labelId="469">威客安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/baidu" labelId="471">百度安全应急响应中心</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/qyaqll" labelId="315">安全理论</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/qyaqyw" labelId="317">安全运维</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/webaq" labelId="263">Web安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/wzsjaq" labelId="264">数据安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/wzfwqaq" labelId="265">服务器安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/khdrjaq" labelId="267">软件安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/khdxtaq" labelId="266">系统安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/txaqyy" labelId="268">安全运营</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/txaqzn" labelId="269">安全智能</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/txyaq" labelId="270">云安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/txwxaq" labelId="271">无线安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/android" labelId="272">Android安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/ios" labelId="273">iOS安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/znqc" labelId="274">智能汽车</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/znjj" labelId="275">智能家居</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/qtznyj" labelId="276">其他智能硬件</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/aqwx" labelId="277">安全威胁</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/aqfh" labelId="278">安全防护</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/aqgl" labelId="279">安全管理</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/aqpj" labelId="281">安全普及</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/xall" labelId="280">信安理论</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/qsnaq" labelId="427">青少年安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses" labelId="472">区块链安全</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/pwn" labelId="395">Pwn</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/mics" labelId="403">Misc</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/web" labelId="419">Web</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses/reverse" labelId="429">Reverse</a>
                                                                                                            </span>
							                                <span class="lab ">
<!--										<a href="--><!--">--><!--</a>-->
                                                                                                                        <a href="https://www.ichunqiu.com/courses" labelId="473">CTF入门</a>
                                                                                                            </span>
																			<div class="slidedown">更多</div>	
					</div>
				</div>
				<div class="direction difficulty" data-label="">
					<div class="leftPart">
						<span class="tag">难度：</span>
						<span class="lab all active">
<!--                            <a href="--><!--">全部</a>-->
                                                                                                                                        <a href="https://www.ichunqiu.com/courses">全部</a>
                                                                                                						</span>
					</div>
					<div class="typeList">
																			<span class="lab ">
<!--								<a href="--><!--">--><!--</a>-->
                                                                                                                                                        <a href="https://www.ichunqiu.com/courses/nandu-chu" degree="1">初级</a>
                                                                                                                                        </span>
													<span class="lab ">
<!--								<a href="--><!--">--><!--</a>-->
                                                                                                                                                        <a href="https://www.ichunqiu.com/courses/nandu-zhong" degree="2">中级</a>
                                                                                                                                        </span>
													<span class="lab ">
<!--								<a href="--><!--">--><!--</a>-->
                                                                                                                                                        <a href="https://www.ichunqiu.com/courses/nandu-gao" degree="3">高级</a>
                                                                                                                                        </span>
											</div>
				</div>
				<div class="direction isExpTab" data-label="">
					<div class="leftPart">
						<span class="tag">实验：</span>
						<span class="lab all active">
<!--							<a href="--><!--">全部</a>-->
                                                                                                                                        <a href="https://www.ichunqiu.com/courses">全部</a>
                                                                                                                        </span>
					</div>
					<div class="typeList">
																			<span class="lab ">
<!--								<a href="--><!--">--><!--</a>-->
                                                                                                                                                        <a href="https://www.ichunqiu.com/courses/shiyan-yes" isExp="1">是</a>
                                                                                                                                        </span>
													<span class="lab ">
<!--								<a href="--><!--">--><!--</a>-->
                                                                                                                                                        <a href="https://www.ichunqiu.com/courses/shiyan-no" isExp="2">否</a>
                                                                                                                                        </span>
											</div>
				</div>
				<div class="direction test isOpenTab" data-label="">
					<div class="leftPart">
						<span class="tag">收费：</span>
						<span class="open all active">
<!--							<a href="--><!--">全部</a>-->
															                                                                            <a href="https://www.ichunqiu.com/courses">全部</a>
                                    															                        </span>
					</div>
					<div class="typeList">
																			<span class="lab ">
<!--								<a href="--><!--">--><!--</a>-->
																	                                                                                    <a href="https://www.ichunqiu.com/courses/open-no" isOpen="1">是</a>
                                        																	                            </span>
													<span class="lab ">
<!--								<a href="--><!--">--><!--</a>-->
																	                                                                                    <a href="https://www.ichunqiu.com/courses/open-yes" isOpen="2">否</a>
                                        																	                            </span>
											</div>
				</div>
				
				<div class="controlMenu">
					<ul>
					<!--																	<li class="menutitle ">
														<span><a href="javascript:;">最新</a></span>
													</li>
																	<li class="menutitle ">
														<span><a href="javascript:;">最热</a></span>
													</li>
																	<li class="menutitle ">
														<span><a href="javascript:;">好评</a></span>
													</li>
																	<li class="menutitle ">
														<span><a href="javascript:;">价格</a></span>
													</li>
					-->
						<li class="menutitle border1" data-label="1" data-sort=""><span>最新</span><span class="icn"></span></li>
						<li class="menutitle border1" data-label="2" data-sort=""><span>最热</span><span class="icn"></span></li>
						<li class="menutitle" data-label="3" data-sort=""><span>好评</span><span class="icn"></span></li>
						<li class="menutitle" data-label="4" data-sort=""><span>价格</span><span class="icn"></span></li>						
					</ul>
					<div class="pageTop">
						<a href="javascript:;"><span class="pageTopleft"></span></a>
						<span class="pageNumber">1</span>&nbsp;/&nbsp;<span class="total">19</span>
						<a href="javascript:;"><span class="pageTopright"></span></a>
					</div>
				</div>
			</div>
			<!--模块-->
			<div class="coursesdiv">
				<ul class="course-box">
																										<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63929" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1537492799040.jpg" alt="AFL模糊测试实战">
												</a>
																									<div class='follow' data-cid="63929" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="AFL模糊测试实战" onclick="javascript:window.open('https://www.ichunqiu.com/course/63929')">AFL模糊测试实战</div>
																											
																													<div class="favorate" course-data="63929" cou-data="AFL模糊测试实战" data-favo="0" style="cursor: pointer;">199元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="3课时8分钟">3课时8分钟</span></div>
																										<div class="comment">662人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63838" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1536558698866.jpg" alt="Web安全从入门到“放弃”">
												</a>
																									<div class='follow' data-cid="63838" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="Web安全从入门到“放弃”" onclick="javascript:window.open('https://www.ichunqiu.com/course/63838')">Web安全从入门到“放弃”</div>
																											
																													<div class="favorate" course-data="63838" cou-data="Web安全从入门到“放弃”" data-favo="0" style="cursor: pointer;">99元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="51课时20分钟">51课时20分钟</span></div>
																										<div class="comment">11312人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63615" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1534125690299.jpg" alt="企业安全最佳实践">
												</a>
																									<div class='follow' data-cid="63615" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="企业安全最佳实践" onclick="javascript:window.open('https://www.ichunqiu.com/course/63615')">企业安全最佳实践</div>
																											
																													<div class="favorate" course-data="63615" cou-data="企业安全最佳实践" data-favo="0" style="cursor: pointer;">699元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="45课时139分钟">45课时139分钟</span></div>
																										<div class="comment">14217人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd none">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63378" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1532914517386.jpg" alt="组网技术与安全基础">
												</a>
																									<div class='follow' data-cid="63378" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="组网技术与安全基础" onclick="javascript:window.open('https://www.ichunqiu.com/course/63378')">组网技术与安全基础</div>
																											
																													<div class="favorate" course-data="63378" cou-data="组网技术与安全基础" data-favo="0" style="cursor: pointer;">150元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="195课时289分钟">195课时289分钟</span></div>
																										<div class="comment">29464人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/58741" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1512721875322.jpg" alt="Android应用加固保护开发入门">
												</a>
																									<div class='follow' data-cid="58741" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="Android应用加固保护开发入门" onclick="javascript:window.open('https://www.ichunqiu.com/course/58741')">Android应用加固保护开发入门</div>
																											
																													<div class="favorate" course-data="58741" cou-data="Android应用加固保护开发入门" data-favo="0" style="cursor: pointer;">499元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="26课时897分钟">26课时897分钟</span></div>
																										<div class="comment">94264人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63609" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1533524694977.jpg" alt="Windows系统操作安全加固">
												</a>
																									<div class='follow' data-cid="63609" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="Windows系统操作安全加固" onclick="javascript:window.open('https://www.ichunqiu.com/course/63609')">Windows系统操作安全加固</div>
																											
																													<div class="favorate" course-data="63609" cou-data="Windows系统操作安全加固" data-favo="0" style="cursor: pointer;">199元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="50课时177分钟">50课时177分钟</span></div>
																										<div class="comment">17671人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/59281" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1511765084539.jpg" alt="教你玩转XSS漏洞">
												</a>
																									<div class='follow' data-cid="59281" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="教你玩转XSS漏洞" onclick="javascript:window.open('https://www.ichunqiu.com/course/59281')">教你玩转XSS漏洞</div>
																											
																													<div class="favorate" course-data="59281" cou-data="教你玩转XSS漏洞" data-favo="0" style="cursor: pointer;">199元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="15课时358分钟">15课时358分钟</span></div>
																										<div class="comment">194537人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd none">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63926" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1536550439297.jpg" alt="【Struts2-057】远程代码执行漏洞（CVE-2018-11776）">
												</a>
																									<div class='follow' data-cid="63926" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="【Struts2-057】远程代码执行漏洞（CVE-2018-11776）" onclick="javascript:window.open('https://www.ichunqiu.com/course/63926')">【Struts2-057】远程代码执行漏洞（CVE-2018-11776）</div>
																											
																													<div class="favorate" course-data="63926" cou-data="【Struts2-057】远程代码执行漏洞（CVE-2018-11776）" data-favo="0" style="cursor: pointer;">免费</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="1课时11分钟">1课时11分钟</span></div>
																										<div class="comment">5455人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63755" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1534900621734.jpg" alt="VMWare 虚拟机基础">
												</a>
																									<div class='follow' data-cid="63755" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="VMWare 虚拟机基础" onclick="javascript:window.open('https://www.ichunqiu.com/course/63755')">VMWare 虚拟机基础</div>
																											
																													<div class="favorate" course-data="63755" cou-data="VMWare 虚拟机基础" data-favo="0" style="cursor: pointer;">99元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="25课时114分钟">25课时114分钟</span></div>
																										<div class="comment">16868人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/58421" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1498526461293.jpg" alt="打造你的铜墙铁壁，Linux防火墙编写与原理分析">
												</a>
																									<div class='follow' data-cid="58421" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="打造你的铜墙铁壁，Linux防火墙编写与原理分析" onclick="javascript:window.open('https://www.ichunqiu.com/course/58421')">打造你的铜墙铁壁，Linux防火墙编写与原理分析</div>
																											
																													<div class="favorate" course-data="58421" cou-data="打造你的铜墙铁壁，Linux防火墙编写与原理分析" data-favo="0" style="cursor: pointer;">499元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="41课时345分钟">41课时345分钟</span></div>
																										<div class="comment">50830人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63901" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1535612851617.jpg" alt="Nmap渗透测试技术入门篇">
												</a>
																									<div class='follow' data-cid="63901" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="Nmap渗透测试技术入门篇" onclick="javascript:window.open('https://www.ichunqiu.com/course/63901')">Nmap渗透测试技术入门篇</div>
																											
																													<div class="favorate" course-data="63901" cou-data="Nmap渗透测试技术入门篇" data-favo="0" style="cursor: pointer;">69元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="13课时36分钟">13课时36分钟</span></div>
																										<div class="comment">17368人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd none">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63088" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1531274500399.jpg" alt="区块链历史安全事件渗透分析">
												</a>
																									<div class='follow' data-cid="63088" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="区块链历史安全事件渗透分析" onclick="javascript:window.open('https://www.ichunqiu.com/course/63088')">区块链历史安全事件渗透分析</div>
																											
																													<div class="favorate" course-data="63088" cou-data="区块链历史安全事件渗透分析" data-favo="0" style="cursor: pointer;">199元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="15课时83分钟">15课时83分钟</span></div>
																										<div class="comment">23079人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63057" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1529631635924.jpg" alt="Burp  Suite之综合实战应用">
												</a>
																									<div class='follow' data-cid="63057" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="Burp  Suite之综合实战应用" onclick="javascript:window.open('https://www.ichunqiu.com/course/63057')">Burp  Suite之综合实战应用</div>
																											
																													<div class="favorate" course-data="63057" cou-data="Burp  Suite之综合实战应用" data-favo="0" style="cursor: pointer;">99元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="6课时37分钟">6课时37分钟</span></div>
																										<div class="comment">44058人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/62897" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1529378008166.jpg" alt="Metasploit入门到精通">
												</a>
																									<div class='follow' data-cid="62897" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="Metasploit入门到精通" onclick="javascript:window.open('https://www.ichunqiu.com/course/62897')">Metasploit入门到精通</div>
																											
																													<div class="favorate" course-data="62897" cou-data="Metasploit入门到精通" data-favo="0" style="cursor: pointer;">219元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="25课时129分钟">25课时129分钟</span></div>
																										<div class="comment">42758人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/59711" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1530508689610.jpg" alt="中国菜刀实例剖析">
												</a>
																									<div class='follow' data-cid="59711" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="中国菜刀实例剖析" onclick="javascript:window.open('https://www.ichunqiu.com/course/59711')">中国菜刀实例剖析</div>
																											
																													<div class="favorate" course-data="59711" cou-data="中国菜刀实例剖析" data-favo="0" style="cursor: pointer;">109元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="5课时27分钟">5课时27分钟</span></div>
																										<div class="comment">42106人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd none">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63762" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1534917879063.jpg" alt="密码学基础概述">
												</a>
																									<div class='follow' data-cid="63762" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="密码学基础概述" onclick="javascript:window.open('https://www.ichunqiu.com/course/63762')">密码学基础概述</div>
																											
																													<div class="favorate" course-data="63762" cou-data="密码学基础概述" data-favo="0" style="cursor: pointer;">免费</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="1课时37分钟">1课时37分钟</span></div>
																										<div class="comment">60847人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/993" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/002/993.jpg" alt="北航教授讲密码学基础">
												</a>
																									<div class='follow' data-cid="993" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="北航教授讲密码学基础" onclick="javascript:window.open('https://www.ichunqiu.com/course/993')">北航教授讲密码学基础</div>
																											
																													<div class="favorate" course-data="993" cou-data="北航教授讲密码学基础" data-favo="0" style="cursor: pointer;">299元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="37课时293分钟">37课时293分钟</span></div>
																										<div class="comment">71441人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/63212" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1532921757090.jpg" alt="CTF精品实战课程">
												</a>
																									<div class='follow' data-cid="63212" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="CTF精品实战课程" onclick="javascript:window.open('https://www.ichunqiu.com/course/63212')">CTF精品实战课程</div>
																											<div class="favorate" course-data="63212" cou-data="CTF精品实战课程" data-favo="0" style="cursor: pointer;">企安殿专属</div>
																									</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="58课时1143分钟">58课时1143分钟</span></div>
																										<div class="comment">65534人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/57007" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1512721847117.jpg" alt="Android应用逆向基础与案例分析">
												</a>
																									<div class='follow' data-cid="57007" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="Android应用逆向基础与案例分析" onclick="javascript:window.open('https://www.ichunqiu.com/course/57007')">Android应用逆向基础与案例分析</div>
																											
																													<div class="favorate" course-data="57007" cou-data="Android应用逆向基础与案例分析" data-favo="0" style="cursor: pointer;">499元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="16课时516分钟">16课时516分钟</span></div>
																										<div class="comment">77157人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
																					<li class="courseonetd none">
																<div class="coursediv" align="center">	
										<div class="courseone" align="left">
											<div align="center" class="bgimg" data-yenjoy="lesson">
												<a class="courseImg" href="https://www.ichunqiu.com/course/61577" target="_blank">
													<img src="https://static2.ichunqiu.com/icq/resources/fileupload/course/1526952611773.jpg" alt="电子取证">
												</a>
																									<div class='follow' data-cid="61577" data-fav="0"></div>
																							</div>
											<div class="coursedesc" align="left">
												<div class="one">
													<div style="width: 180px" class="coursename" title="电子取证" onclick="javascript:window.open('https://www.ichunqiu.com/course/61577')">电子取证</div>
																											
																													<div class="favorate" course-data="61577" cou-data="电子取证" data-favo="0" style="cursor: pointer;">59元</div>
																										</div>
												<div class="two">
																											<div class="producer"><span class="prostatus active"></span><span title="6课时95分钟">6课时95分钟</span></div>
																										<div class="comment">54479人学习</div>
												</div>
											</div>
										</div>
									</div>
								</li>
															</ul>
				<input type="hidden" value="all" id="direction">
				<input type="hidden" value="all" id="classname">
				<input type="hidden" value="all" id="difficulty">
				<input type="hidden" value="all" id="isexp">
                <input type="hidden" value="all" id="ispay">
				<input type="hidden" value="0" id="orderby">
				<input type="hidden" value="2" id="sort">
				<input type="hidden" value="365" class="dataTotal">
				<div id="page" style="text-align:center;margin-bottom:30px;">
                    <ul class="paginorange" style="margin: 10px 0px;">
                    </ul>
				</div>
			</div>
		</div>
		<input type="hidden" class="mark" value="0">
		<input type="hidden" id="headeract" value="1">
	<link rel="stylesheet" href="https://static2.ichunqiu.com/icq/resources/css/common/footer.css?v=20180108" type="text/css">
<link rel="stylesheet" href="https://static2.ichunqiu.com/icq/resources/css/common/loginReg.css?v=e9d4s86g7a" type="text/css">
<div class="footer">
    <div class="footerTop">
        <a href="javascript:;" class="weibo">
            <div class="weibo_box"></div>
        </a>
        <a href="javascript:;" class="weixin">
            <div class="weixin_box"></div>
        </a>
    </div>
    <div class="footercenWrap">
        <div class="footercen">
            <a href="https://www.ichunqiu.com/default/introduce" target="_blank">了解i春秋</a>
            <a href="https://www.ichunqiu.com/default/joinus" target="_blank">加入i春秋</a>
            <a href="https://www.ichunqiu.com/recruit" target="_blank">讲师招募</a>
            <a href="https://www.ichunqiu.com/src" target="_blank">有信众测</a>
            <a href="https://www.ichunqiu.com/xietongyuren" target="_blank">协同育人</a>
            <a href="https://www.ichunqiu.com/default/help" target="_blank">帮助中心</a>
            <a href="https://www.ichunqiu.com/default/disclaimer" target="_blank">用户协议</a>
            <a href="mailto:">邮箱：kefu@ichunqiu.com</a>
            <span>QQ群：827546392、556040588、234714762</span>
        </div>
    </div>
    <p style="line-height: normal;padding-top: 20px;padding-bottom: 5px;">
        <span>版权所有</span>
        <span>北京五一嘉峪科技有限公司</span>
    </p>
    <p style="line-height: normal; border: none;padding-bottom: 5px;">
        <span style="margin: 0;">地址:</span>
        <span>海淀区中关村软件广场C座</span>
    </p>
    <p style="border: none;line-height: normal;">
        <span>京ICP证150695号</span>
        <span>京ICP备15029557号</span>
        <span>京公网安备11010802017937号</span>
    </p>
</div>
<div id="loginReg"></div>
<div style="display: none;">
    <!--友盟统计代码-->
    <script src="https://s13.cnzz.com/z_stat.php?id=1262179648&web_id=1262179648" language="JavaScript"></script>
</div>
<script>
    var base_url = 'https://www.ichunqiu.com/';
    var resource_url = 'https://static2.ichunqiu.com/icq/';
    var exam_url = 'https://www.ichunqiu.com/';
    var user_site_url = 'https://user.ichunqiu.com/';
    var bbs_site_url = 'https://bbs.ichunqiu.com/';
    var qad_url = "https://www.ichunqiu.com/qad/";
    var uid = '';
    var special = '&,%,>,<';
    var ut = '';
    var yzmShow = '';

    //用户体系
    var business_usersystem = '2';
    var ws_server = 'wss://msg.ichunqiu.com';
    var userHead = 'https://static2.ichunqiu.com/icq/resources/upload/images/DefaultUserIcon.png'
    var username = '';
</script>
<!-- 插件 js -->
<script language="JavaScript" type="text/javascript"
        src="https://static2.ichunqiu.com/icq/resources/js/plugin/jquery1.8.3.min.js"></script>
<script language="JavaScript" type="text/javascript"
        src="https://static2.ichunqiu.com/icq/resources/js/plugin/jQuery.ajax.js"></script>
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/plugin/bootstrap.min.js"></script>

<script src="https://static2.ichunqiu.com/icq/resources/js/plugin/jquery.validate.min.js"></script>
<script type="text/javascript"
        src="https://static2.ichunqiu.com/icq/resources/js/plugin/jquery.mCustomScrollbar.concat.min.js"></script>
<!-- 插件 加密js -->
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/plugin/mix.js"></script>
<!-- 插件 小i导航泉币商城兑换填写收件地址 -->        
<script language="JavaScript" type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/home/area.js"></script>
<!-- svg 头部导航相关svg -->
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/common/header_svg.js?v=38eaf31847"></script>
<!-- 公共js -->
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/common/component.js?v=e93h4d76dgf"></script>
<!-- 注册登录 -->
<script src="https://static2.ichunqiu.com/icq/resources/js/common/loginReg.js?v=f2e92af169"></script>
<!-- 头部js -->
<script src="https://static2.ichunqiu.com/icq/resources/js/common/header.js?v=e8f35da9s2a"></script>
<!-- 独立功能 优享会员标识(课程/会员) -->
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/common/yenjoy.js?v=7c78ca004ac0c8e984c8404315d992a5"></script>
<!-- 用户体系小I -->
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/common/exp1.js?v=7b12025408"></script>
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/IRD/IRD-i.js?v=bb644b03ae5da915505e3f6da2d08d46"></script>
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/IRD/robot.js?v=fe6c8d40b0ca17c63a1bd8b4e96e9cc5"></script>
<!--企安殿4.0新用户登陆js-->
<script src="https://static2.ichunqiu.com/icq/resources/js/company/qad/qadfyd.js"></script>
<!--腾讯统计-->
<script type="text/javascript" src="https://tajs.qq.com/stats?sId=62520791" charset="UTF-8"></script>
<!--百度统计-->
<script>
    var _hmt = _hmt || [];
    (function () {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?2d0601bd28de7d49818249cf35d95943";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();
</script>
<!--百度自动推送代码-->
<script>

(function(){
	if(window.location.host == "www.ichunqiu.com"){
		var bp = document.createElement('script');

	    var curProtocol = window.location.protocol.split(':')[0];
	
	    if (curProtocol === 'https') {
	
	        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';        
	
	    }
	
	    else {
	
	        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
	
	    }
	
	    var s = document.getElementsByTagName("script")[0];
	
	    s.parentNode.insertBefore(bp, s);

	}
})();

</script>
<script type="text/javascript">
<!--
	$(function(){
		//判断企安殿用户接口
		$('.qiandian').empty();
		$.post(base_url+'company/qad/iscompany', {}, function(user){
			if(user){
				if(user.status != 2 && user.status != 3 && user.status != 5){
					$('.qiandian').append('<i class="ficon qads"></i><a href="javascript:;" onclick="enterqiandian()" class="enterqadfont">进入企安殿</a>');
				}
			}
		}, 'json');		
		//判断培训机构助教接口
		$('.pxzhujiao').empty();
		$.post(base_url+'train/Common/ajaxTrainUser', {}, function(data){
			if(data.status == 1){
				if(data.data.UserType == 1){
					$('.pxzhujiao').append('<i class="ficon zjs"></i><a href='+data.data.Url+'>进入助教后台</a>');
				}
			}else{
				
			}
		}, 'json');		
	});

    function enterqiandian() {
        $.post(base_url + 'company/qad/iscompany', {}, function (user) {
            if (user) {
                if (user.status == 2) {
                    ShowLoginDialog();
                } else if (user.status == 4 || user.status == 5) {
                    FailureDialog(user.msg);
                } else {
                    window.location.href = user.url;
                }
            }
        }, 'json');
    }
    //-->
</script>
</body>
<script type="text/javascript" src="https://static2.ichunqiu.com/icq/resources/js/courses/index.js?v=f898cbd3a9"></script>
</html>

'''

p = r'<div style="width: 180px" class="coursename" title="(.*?)" onclick='
title = re.findall(p,html)

print(title)