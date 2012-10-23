	

$(document).ready(function() {
	$('#btn-homepage-login').click(function() {
			$('#login-spinner').css({display: 'block'});
			$('#links').html('');
			var link = $('#link').val();
			$("#btn-homepage-login").hide();
			var uri='/ytdownloader?url='.concat(link)
			$.ajax({
				url: uri,
				type: 'POST',
				data:{ },
			success: function(data) {
				var k;
				$('#links1').html('');
				$('#login-spinner').css({display: 'none'});
				$('#links').append('<div id="ll" class="first">'+data['title']+'</div>' )
				for (i in data['name'])
				{	k=parseInt(i)+1;
					$('#links').append('<div id="ll">' + '<a href="'+ data['link'][i] +'" title="'+data['title']+'.'+data['format'][i] +'">'+'>> Download '+data['name'][i] + ' << </a></div>');
					
				}
					$("#btn-homepage-login").show();
			}
		}).fail(function() { 
			 $('#login-spinner').css({display: 'none'});
			 $("#btn-homepage-login").show();
			 $('#links1').append('Link Invalid/Service Temporarily Down');
		});
	});
});
