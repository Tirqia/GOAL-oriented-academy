// 1. ობიექტი, რომელიც ასახავს წიგნს სათაურის, ავტორისა და გამოცემის წლის თვისებებით.
let book = {
    title: "დათა თუთაშხია",
    author: "ჭაბუა ამირეჯიბი",
    year: 1973
};

// 2. დაამატეთ ახალი თვისება არსებულ ობიექტს.
book.genre = "რომანი";

// 3. ობიექტიდან თვისების წაშლა.
delete book.year;

// 4. ობიექტში საკუთრების მნიშვნელობის წვდომა და ბეჭდვა.
console.log(book.title); 

// 5. შეამოწმეთ არის თუ არა თვისება ობიექტში.
console.log("author" in book);

// 6. გაიმეორეთ ობიექტის ყველა თვისება და დაბეჭდეთ მათი მნიშვნელობები.
for (let key in book) {
    console.log(book[key]);
}

// 7. შექმენით ობიექტების მასივი, თითოეული წარმოადგენს პიროვნებას სახელისა და ასაკის თვისებების მქონე.
let people = [
    { name: "დათა", age: 42 },
    { name: "მუშნი", age: 29 },
    { name: "მოსე", age: 40 }
];

// 8. იპოვეთ ობიექტის სიგრძე (თვისებების რაოდენობა).
console.log(Object.keys(book).length)

// 9. შექმენით ობიექტი წყობილი ობიექტებით და შედით თვისებაზე წყობილი ობიექტიდან.
let library = {
    Section: {
        expression: {
            word: "რა ქენი გუდუნა ეს"
        }
    }
};
console.log(library.section.expression.word); 

// 10. ობიექტის გადაქცევა მისი თვისებების მნიშვნელობების მასივში.
let bookValues = Object.values(book);
console.log(bookValues);

// 11. შექმენით რიცხვების მასივი 1-დან 10-მდე.
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// 12. დაამატეთ ელემენტი მასივის ბოლოს.
numbers.push(11);
console.log(numbers); 

// 13. დაამატეთ ელემენტი მასივის დასაწყისში.
numbers.unshift(0);
console.log(numbers); 

// 14. ამოიღეთ მასივის ბოლო ელემენტი.
numbers.pop();
console.log(numbers); 

// 15. ამოიღეთ მასივის პირველი ელემენტი.
numbers.shift();
console.log(numbers);

// 16. იპოვეთ მასივის სიგრძე.
console.log(numbers.length); // 10

// 17. მასივის მესამე ელემენტზე წვდომა.
console.log(numbers[2]); // 3

// 18. გაიმეორეთ მასივი და ამობეჭდეთ თითოეული ელემენტი.
for (let number of numbers) {
    console.log(number);
}

// 19. შექმენით ახალი მასივი არსებული მასივის თითოეული ელემენტის გაორმაგებით.
let doubledNumbers = numbers.map(num => num * 2);
console.log(doubledNumbers); 

// 20. შეცვალეთ ელემენტების თანმიმდევრობა მასივში.
numbers.reverse();
console.log(numbers);
