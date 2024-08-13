// 1. ცივილური თარიღი "MM/DD/YYYY" ფორმატში
function getDateFormatted() {
    let now = new Date();
    let month = String(now.getMonth() + 1).padStart(2, '0');
    let day = String(now.getDate()).padStart(2, '0');
    let year = now.getFullYear();
    return `${month}/${day}/${year}`;
}
console.log(getDateFormatted());

// 2. მიმდინარე დრო "HH:MM" ფორმატში
function getTimeFormatted() {
    let now = new Date();
    let hours = String(now.getHours()).padStart(2, '0');
    let minutes = String(now.getMinutes()).padStart(2, '0');
    return `${hours}:${minutes}`;
}
console.log(getTimeFormatted());

// 3. რიცხვის მიხედვით კვირის დღის დაბრუნება
function getDayName(number) {
    const days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"];
    return days[number - 2];
}
console.log(getDayName(5)); 

// 4. დღეების რაოდენობა ორ თარიღს შორის
function calculateDays(date1, date2) {
    let start = new Date(date1);
    let end = new Date(date2);
    let difference = Math.abs(end - start);
    return Math.ceil(difference / (1000 * 60 * 60 * 24));
}
console.log(calculateDays("2024-01-01", "2024-07-31"));

// 5. თარიღი "YYYY-MM-DD" ფორმატში
function formatDate(date) {
    let year = date.getFullYear();
    let month = String(date.getMonth() + 1).padStart(2, '0');
    let day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}
console.log(formatDate(new Date()));

// 6. ორ თარიღს შორის შედარება
function compareDates(date1, date2) {
    let d1 = new Date(date1);
    let d2 = new Date(date2);
    if (d1 < d2) return "პირველი თარიღი უფრო ადრეა";
    if (d1 > d2) return "მეორე თარიღი უფრო ადრე";
    return "ორივე თარიღი ემთხვევა ერთმანეთს";
}
console.log(compareDates("2023-11-06", "2024-07-31"));

// 7. თვეების რაოდენობა კონკრეტულ თვეში
function getDaysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}
console.log(getDaysInMonth(4, 2024)); 

// 8. დროის სხვაობა თარიღამდე
function timeAgo(dateStr) {
    let now = new Date();
    let pastDate = new Date(dateStr);
    let diff = now - pastDate;
    let days = Math.floor(diff / (1000 * 60 * 60 * 24));
    if (days > 30) return `${Math.floor(days / 30)} თვის წინ`;
    if (days > 0) return `${days} დღის წინ`;
    return "დღეს";
}
console.log(timeAgo("2023-07-31"));

// 9. დღეების რაოდენობა მომდევნო დაბადების დღემდე
function daysToNextBirthday(birthDate) {
    let today = new Date();
    let nextBirthday = new Date(birthDate);
    nextBirthday.setFullYear(today.getFullYear());
    if (today > nextBirthday) nextBirthday.setFullYear(today.getFullYear() + 1);
    return Math.ceil((nextBirthday - today) / (100 * 60 * 60 * 24));
}
console.log(daysToNextBirthday("2008-01-10"));

// 10. ასაკის გამოთვლა წლების მიხედვით
function getAge(birthDate) {
    let today = new Date();
    let birth = new Date(birthDate);
    let age = today.getFullYear() - birth.getFullYear();
    if (today.getMonth() < birth.getMonth() || (today.getMonth() === birth.getMonth() && today.getDate() < birth.getDate())) {
        age--;
    }
    return age;
}
console.log(getAge("2008-01-10"));
