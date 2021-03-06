//$(document).ready(function(){
jQuery(function($) {


	$('#complexicator').validate({
		rules: {
			age: {
				digits: true,
				max: 160,
				required: true,
			},
			gender: "required",
			status: "required",
			ignorance: {
				digits: true,
				max: 100,
				required: true
			},
			money_have: {
				digits: true,
				required: true
			},
			money_wants: {
				digits: true,
				required: true
			},
			money_spent: {
				digits: true,
				required: true
			},
			popularity_online: {
				digits: true,
				max: 100,
				required: true
			},
			rl_friends: "required",
		},

		messages: {
			age: {
				digits: "Age should be a whole number, written with digits.",
				max: "Surely your're not more than 160 years old?",
				required: "Don't worry, you're definitely not too old"
			},
			gender: "Male or female, or the closest one.",
			status: "I won't judge, pick the closest one.",
			ignorance: {
				digits: "Use only numbers between 0 and 100.",
				required: "Estimate your ignorance on a scale from 0 to 100.",
				max: "Pick a number between 0 and 100."
			},
			money_have: {
				digits: "Use only numbers, please.",
				required: "Estimate the amount you currently have with numbers.",
			},
			money_wants: {
				digits: "Use only numbers, please.",
				required: "Estimate the amount you currently want with numbers.",
			},
			money_spent: {
				digits: "Use only numbers, please.",
				required: "Estimate the amount you spent today with numbers.",
			},
			popularity_online: {
				digits: "Your Klout score is a number between 1 and 100. Write 0 if you don't know what this is.",
				required: "Your Klout score is a number between 1 and 100. Write 0 if you don't know what this is.",
				max: "Can't have a score greater than 100."
			},
			rl_friends: "How many people could you call in the middle of the night for a flat tire?",
		},
		highlight: function(element) {
			$(element).closest('.form-group').removeClass('has-success').addClass('has-error');
		},
		success: function(element) {
			element
			.text("All good!").addClass('hidden')
			.closest('.form-group').removeClass('has-error').addClass('has-success');
		},
        errorPlacement: function (error, element) {
            var name = element.attr("name");
            $(".error-label-" + name).append(error);

     },

	});
	

}); // end document.ready
