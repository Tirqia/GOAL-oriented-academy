const weather = {
    location: "ZUGDIDI",
    temperature: "28°C",
};

Object.entries(weather).forEach(([key, value]) => {
    console.log(`${key}: ${value}`);
});
