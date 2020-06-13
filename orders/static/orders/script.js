document.addEventListener('DOMContentLoaded', () => {

	function hideAllToppings() {
		document.querySelector('#toppings-wrap1').style.display = 'none';
		document.querySelector('#toppings-wrap2').style.display = 'none';
		document.querySelector('#toppings-wrap3').style.display = 'none';
	}

	function hidePizzaSelectors() {
		document.querySelector('#size-wrap').style.display = 'none';
		document.querySelector('#pizza-wrap').style.display = 'none';
		document.querySelector('#topping-number-wrap').style.display = 'none';
		hideAllToppings();
	}

	function showPizzaSelectors() {
		document.querySelector('#size-wrap').style.display = 'block';
		document.querySelector('#pizza-wrap').style.display = 'block';
		document.querySelector('#topping-number-wrap').style.display = 'block';
	}

	function hideSubSelectors() {
		document.querySelector('#size-wrap').style.display = 'none';
		document.querySelector('#subs-wrap').style.display = 'none';
		document.querySelector('#extra-all-wrap').style.display = 'none';
		document.querySelector('#extra-steak-wrap').style.display = 'none';
	}

	function showSubSelectors() {
		document.querySelector('#size-wrap').style.display = 'block';
		document.querySelector('#subs-wrap').style.display = 'block';
		document.querySelector('#extra-all-wrap').style.display = 'block';
	}

	document.querySelector('#sub-name').onchange = () => {
			if (document.querySelector('#sub-name').value === 'steak+cheese') {
				document.querySelector('#extra-steak-wrap').style.display = 'block';
			} else {
				document.querySelector('#extra-steak-wrap').style.display = 'none';
			}
		};

	function showPastaSelectors() {
		document.querySelector('#pasta-wrap').style.display = 'block';
	}

	function hidePastaSelectors() {
		document.querySelector('#pasta-wrap').style.display = 'none';
	}

	function showSaladSelectors() {
		document.querySelector('#salad-wrap').style.display = 'block';
	}

	function hideSaladSelectors() {
		document.querySelector('#salad-wrap').style.display = 'none';
	}

	function showDinnerPlateSelectors() {
		document.querySelector('#dinner-plate-wrap').style.display = 'block';
		document.querySelector('#size-wrap').style.display = 'block';
	}

	function hideDinnerPlateSelectors() {
		document.querySelector('#dinner-plate-wrap').style.display = 'none';
		document.querySelector('#size-wrap').style.display = 'none';
	}



	document.querySelector('#food-type').onchange = () => {
		const food_type = document.querySelector('#food-type').value;

		switch(food_type) {
			case 'pizza':
				hideSubSelectors();
				hidePastaSelectors();
				hideSaladSelectors();
				hideDinnerPlateSelectors();
				showPizzaSelectors();
				break;
			case 'sub':
				hidePizzaSelectors();
				hidePastaSelectors();
				hideSaladSelectors();
				hideDinnerPlateSelectors();
				showSubSelectors();
				break;
			case 'pasta':
				hidePizzaSelectors();
				hideSubSelectors();
				hideSaladSelectors();
				hideDinnerPlateSelectors();
				showPastaSelectors();
				break;
			case 'salad':
				hidePizzaSelectors();
				hideSubSelectors();
				hidePastaSelectors();
				hideDinnerPlateSelectors();
				showSaladSelectors();
				break;
			case 'dinner_plate':
				hidePizzaSelectors();
				hideSubSelectors();
				hidePastaSelectors();
				hideSaladSelectors();
				showDinnerPlateSelectors();
				break;
			default:
				hidePizzaSelectors();
				hideSubSelectors();
				hidePastaSelectors();
				hideSaladSelectors();
				hideDinnerPlateSelectors();
		}
	};

	document.querySelector('#topping-number').onchange = () => {
		const toppings_selected = document.querySelector('#topping-number').value;

		switch(toppings_selected) {
			case '1 topping':
				document.querySelector('#toppings-wrap1').style.display = 'block';
				document.querySelector('#toppings-wrap2').style.display = 'none';
				document.querySelector('#toppings-wrap3').style.display = 'none';
				break;
			case '2 toppings':
				document.querySelector('#toppings-wrap1').style.display = 'block';
				document.querySelector('#toppings-wrap2').style.display = 'block';
				document.querySelector('#toppings-wrap3').style.display = 'none';
				break;
			case '3 toppings':
				document.querySelector('#toppings-wrap1').style.display = 'block';
				document.querySelector('#toppings-wrap2').style.display = 'block';
				document.querySelector('#toppings-wrap3').style.display = 'block';
				break;
			case 'Cheese' || 'Special':
				hideAllToppings();
				break
			default:
				hideAllToppings();
		}
	};

});