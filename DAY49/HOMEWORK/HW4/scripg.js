let obj1 = {
    Name: "ALEKO",
    lastName: "TIRKIA",
    age: 30,
    country: "GEORGIA",
    city: "ZUGDIDI",
    school: "ZUGIDIS NOMER 11 SKOLA"
}
let obj2 = {
    Name: "ALEKO",
    lastName: "TIRKIA",
    age: 30,
    country: "GEORGIA",
    city: "ZUGDIDI",
    school: "ZUGIDIS NOMER 11 SKOLA"
};

function compareObjects(obj1, obj2) {
    if (Object.keys(obj1).length !== Object.keys(obj2).length) {
        return false;
    }

    for (let key in obj1) {
        if (obj1[key] !== obj2[key]) {
            return false;
        }
    }

    return true;
}

console.log(compareObjects(obj1, obj2));
