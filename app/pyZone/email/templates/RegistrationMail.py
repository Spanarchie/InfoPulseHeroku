def getRegHtml():
    html = """\
<p>
<html>
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
   <title>Welcome to InfoPulseCoUk</title>
   <style type="text/css">
   	a {color: #4A72AF;}
	body, #header h1, #header h2, p {margin: 0; padding: 0;}
	#main {border: 1px solid #cfcece;}
	img {display: block;}
	#top-message p, #bottom-message p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
	#header h1 {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
	#header h2 {color: #ffffff !important; font-family: Arial, Helvetica, sans-serif; font-size: 24px; margin-bottom: 0 !important; padding-bottom: 0; }
	#header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
	h1, h2, h3, h4, h5, h6 {margin: 0 0 0.8em 0;}
	h3 {font-size: 28px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
	h4 {font-size: 22px; color: #4A72AF !important; font-family: Arial, Helvetica, sans-serif; }
	h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
	p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
   </style>
</head></p>

<p><body></p>

<p><table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td></p>

<p><table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
		<tr>
			<td align="center">
				<p>Trouble viewing this email? <a href="#">View in Browser</a></p>
			</td>
		</tr>
	</table><!-- top message --></p>

<p><table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
		<tr>
			<td>
				<table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
					<tr>
						<td width="570" bgcolor="7aa7e9"><h1>Welcome to InfoPulseCoUk</h1></td>
					</tr>
					<tr>
						<td width="570" bgcolor="8fb3e9" style="background: url(http://tessat.s3.amazonaws.com/email-bg.jpg);"><h2 style="color:#ffffff!important">You application is being processed...</h2></td>
					</tr>
					<tr>
						<td width="570" align="right" bgcolor="7aa7e9"><p>July 2010</p></td>
					</tr>
				</table><!-- header -->
			</td>
		</tr><!-- header -->

		<tr>
			<td></td>
        </tr>
        <tr>
            <td>
                <table id="content-1" cellpadding="0" cellspacing="0" align="center">
                    <tr>
						<td width="170" valign="top">
							<table cellpadding="5" cellspacing="0">
								<tr><td bgcolor="d0d0d0"><img src="http://tessat.s3.amazonaws.com/coins_small.jpg" width="170" /></td></tr></table>
						</td>
						<td width="15"></td>
						<td width="375" valign="top" colspan="3">
							<h3>All New Site Design</h3>
							<h4>Your application has been sent to your Client Administrator for Verification. Once accepted you will be sent an email to give access to the system and set your security details.</h4>
						</td>
                    </tr>
				</table><!-- content 1 -->
			</td>
		</tr><!-- content 1 -->
		<tr>
			<td>
				<table id="content-2" cellpadding="0" cellspacing="0" align="center">
					<tr>
						<td width="570"><p>Please add infopulse to your NOT junk list, or check your junk mailbox.</p></td>
					</tr>
				</table><!-- content-2 -->
			</td>
		</tr><!-- content-2 -->


	</table><!-- main -->
	<table id="bottom-message" cellpadding="20" cellspacing="0" width="600" align="center">
		<tr>
			<td align="center">
				<p>You are receiving this email because you signed up for Access to the Infopulse system</p>
			</td>
		</tr>
	</table><!-- top message -->
</td></tr></table><!-- wrapper --></p>

<p></body>
</html>
</p>
"""
    return html