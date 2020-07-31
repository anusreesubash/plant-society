$(document).ready(function(){
	$.ajax({
		url: 'http://127.0.0.1:5000/api/post'
	}).done(function(posts){
		$.each(posts, function(index, post){
			let title = post.title;
			$('.list-group').append(`<li class = "list-group-item">${title}</li>`);

			console.log(title);
			console.log(index);
		});
	
	});

 
});
