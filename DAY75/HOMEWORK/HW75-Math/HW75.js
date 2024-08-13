// 1. რანდომული მთელი რიცხვის გენერაცია მინიმუმ და მაქსიმუმ მნიშვნელობებს შორის
function getRandomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
console.log(getRandomInteger(1, 111));

// 2. რიცხვის კვადრატული ფესვის გამოთვლა
function getSquareRoot(number) {
    return Math.sqrt(number);
}
console.log(getSquareRoot(55));

// 3. რიცხვის ახლოს მყოფი მთელი რიცხვის მომრგვალება
function roundToNearestInteger(number) {
    return Math.round(number);
}
console.log(roundToNearestInteger(7.4)); 

// 4. რიცხვის ქვედა მთელ რიცხვზე მომრგვალება
function roundDown(number) {
    return Math.floor(number);
}
console.log(roundDown(4.9)); 

// 5. რიცხვის ზედა მთელ რიცხვზე მომრგვალება
function roundUp(number) {
    return Math.ceil(number);
}
console.log(roundUp(1.7)); 

// 6. რიცხვის ძალა გამოთვლა (მაგ., 2^3)
function power(base, exponent) {
    return Math.pow(base, exponent);
}
console.log(power(2, 7)); 

// 7. რიცხვის აბსოლუტური მნიშვნელობის დაბრუნება
function getAbsoluteValue(number) {
    return Math.abs(number);
}
console.log(getAbsoluteValue(-134)); 

// 8. რიცხვების მასივში ყველაზე დიდი რიცხვის დაბრუნება
function getLargestNumber(array) {
    return Math.max(...array);
}
console.log(getLargestNumber([332, 121, 231, 44, 13]));

// 9. რანდომული ბულიანური მნიშვნელობის გენერაცია (true ან false)
function getRandomBoolean() {
    return Math.random() < 0.5;
}
console.log(getRandomBoolean()); 

// 10. რანდომული RGB ფერის გენერაცია "rgb(r, g, b)" ფორმატში
function getRandomRGBColor() {
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}
console.log(getRandomRGBColor()); 
