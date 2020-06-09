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
			if (document.querySelector('#sub-name').value === 'Steak+Cheese') {
				document.querySelector('#extra-steak-wrap').style.display = 'block';
			} else {
				document.querySelector('#extra-steak-wrap').style.display = 'none';
			}
		};



	document.querySelector('#food-type').onchange = () => {
		const food_type = document.querySelector('#food-type').value;

		switch(food_type) {
			case 'pizza':
				hideSubSelectors();
				showPizzaSelectors();
				break;
			case 'sub':
				hidePizzaSelectors();
				showSubSelectors();
				break;
			case 'dinner_plate':
				hidePizzaSelectors();
				// showDinnerPlateSelectors();
				break;
			case 'pasta':
				hidePizzaSelectors();
				break;
			case 'salad':
				hidePizzaSelectors();
				break;
			default:
				hidePizzaSelectors()
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