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

	document.querySelector('#food-type').onchange = () => {
		const food_type = document.querySelector('#food-type').value;

		switch(food_type) {
			case 'pizza':
				showPizzaSelectors();
				break;
			case 'pasta':
				hidePizzaSelectors();
				break;
			case 'salad':
				hidePizzaSelectors();
				break;
			case 'dinner_plate':
				hidePizzaSelectors();
				document.querySelector('#size-wrap').style.display = 'block';
				break;
			case 'sub':
				hidePizzaSelectors();
				document.querySelector('#size-wrap').style.display = 'block';
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