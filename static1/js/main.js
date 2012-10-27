	
function jso(sss)
{	
	if(!sss.name)
	{
		$('#login-spinner').css({display: 'none'});
        $("#btn-homepage-login").show();
	 	$('#links1').html('');
	 	$('#links').html('');
		$('#links1').append('Link Invalid/Service Temporarily Down, try again');
		return;
	}	
		
	$('#links1').html('');
	$('#login-spinner').css({display: 'none'});
	$('#links').append('<div id="ll" class="first">'+sss.title+'</div>' )
	for (i in sss.name)
		{	k=parseInt(i)+1;
			$('#links').append('<div id="ll">' + '<a href="http://ytdownloader-namitsingal.rhcloud.com/download/'+sss.title +'.'+sss.format[i]+'?url='+ (sss).link[i] +'&format='+sss.format[i]+'">'+'>> Download '+sss.name[i] + ' << </a></div>');
			
		}
	$("#btn-homepage-login").show();
}
$(document).ready(function() {
	$('#btn-homepage-login').click(function() {
			$('#links1').html('');
			$('#links').html('');
			$('#login-spinner').css({display: 'block'});
			var link = $('#link').val();
			$("#btn-homepage-login").hide();
			var uri='http://ytdownloader-namitsingal.rhcloud.com/ytdownloader?url='.concat(link)
			$.ajax({
				dataType:'jsonp',
				url: uri,
				type: 'POST',
				data:{ },
			success: function(data) {
				//$('#links').html('sd');
				/*var k;
				$('#links1').html('');
				$('#login-spinner').css({display: 'none'});
				$('#links').append('<div id="ll" class="first">'+data['title']+'</div>' )
				for (i in data['name'])
				{	k=parseInt(i)+1;
					$('#links').append('<div id="ll">' + '<a href="'+ data['link'][i] +'" title="'+data['title']+'.'+data['format'][i] +'">'+'>> Download '+data['name'][i] + ' << </a></div>');
					
				}
					$("#btn-homepage-login").show();
				*/
			}
			})
	});
});
