let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let list = document.querySelector('.list');
let listCard = document.querySelector('.listCard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

openShopping.addEventListener('click', ()=>{
   body.classList.add('active');
})
closeShopping.addEventListener('click', ()=>{
    body.classList.remove('active');
})

let products = [
    {
        id: 1,
        name: 'The Hidden Hindu',
        image: 'fiction1.jpg',
        price: 120000
    },
    {
        id: 2,
        name: 'The Magic Drum',
        image: 'fiction2.jpg',
        price: 120000
    },
    {
        id: 3,
        name: 'Malgudi Days',
        image: 'fiction3.jpg',
        price: 220000
    },
    {
        id: 4,
        name: 'The English Teacher',
        image: 'fiction4.jpg',
        price: 123000
    },
    {
        id: 5,
        name: 'A House Without Windows',
        image: 'fiction5.jpg',
        price: 320000
    },
    {
        id: 6,
        name: 'Ghachar Ghochar',
        image: 'fiction6.jpg',
        price: 120000
    },
    {
        id: 7,
        name: ' Sea of Poppies',
        image: 'fiction7.jpg',
        price: 120000
    },
{
        id: 8,
        name: 'The Hour of Magic',
        image: 'fiction8.jpg',
        price: 120000
    },
{
        id: 9,
        name: 'One Part Woman',
        image: 'fiction9.jpg',
        price: 120000
    },
    {
        id: 10,
        name: 'BABU BANGLADESH',
        image: 'nfiction1.jpg',
        price: 120000
    },
     {
        id: 3,
        name: 'Autobiography of a Yogi',
        image: 'nfiction3.jpg',
        price: 220000
    },
     {
        id: 4,
        name: 'Tiger of Drass: Capt. Anuj Nayyar, 23, Kargil Hero',
        image: 'nfiction4.jpg',
        price:123000
        },
        {id: 5,name: 'Panchtantra Ki Kahaniyan',image: 'nfiction5.jpg',price: 320000},
        {id: 6,name: 'spoken english',image: 'nfiction6.jpg',price: 120000},
        {id: 7,name: ' empire of moghulbrothers at war',image: 'nfiction7.jpg',price: 120000},
        {id: 8,name: 'under the banyan tree',image: 'nfiction8.jpg',price: 120000},
        {
        id: 9,
        name: 'Constitution and its Working',
        image: 'nfiction9.jpg',
        price:120000
        },
        { id: 19, name: 'Educated: A Memoir', image: 'nfiction11.jpg', price: 220000, category: 'non-fiction' }





];
let listCards  = [];
function initApp(){
    products.forEach((value, key) =>{
        let newDiv = document.createElement('div');
        newDiv.classList.add('item');
        newDiv.innerHTML = `
            <img src="static/${value.image}">
            <div class="title">${value.name}</div>
            <div class="price">${value.price.toLocaleString()}</div>
            <button onclick="addToCart(${key})">Add To Cart</button>`;
        list.appendChild(newDiv);
    })
}
initApp();
function addToCart(key){
    if(listCards[key] == null){
        // copy product form list to list card
        listCards[key] = JSON.parse(JSON.stringify(products[key]));
        listCards[key].quantity = 1;
    }
    reloadCard();
}
function reloadCard(){
    listCard.innerHTML = '';
    let count = 0;
    let totalPrice = 0;
    listCards.forEach((value, key)=>{
        totalPrice = totalPrice + value.price;
        count = count + value.quantity;
        if(value != null){
            let newDiv = document.createElement('li');
            newDiv.innerHTML = `
                <div><img src="static/${value.image}"/></div>
                <div>${value.name}</div>
                <div>${value.price.toLocaleString()}</div>
                <div>
                    <button onclick="changeQuantity(${key}, ${value.quantity - 1})">-</button>
                    <div class="count">${value.quantity}</div>
                    <button onclick="changeQuantity(${key}, ${value.quantity + 1})">+</button>
                </div>`;
                listCard.appendChild(newDiv);
        }
    })
    total.innerText = totalPrice.toLocaleString();
    quantity.innerText = count;
}
function changeQuantity(key, quantity){
    if(quantity == 0){
        delete listCards[key];
    }else{
        listCards[key].quantity = quantity;
        listCards[key].price = quantity * products[key].price;
    }
    reloadCard();
}