/*СКРИПТ ДЛЯ СМЕНЫ ТЕМЫ */

const themeSwitcher = document.getElementById("theme-switcher");

themeSwitcher.addEventListener("click", function() {
  const htmlClassList = document.querySelector("html").classList;

  if (htmlClassList.contains("light-theme")) {
    htmlClassList.remove("light-theme");
    htmlClassList.add("dark-theme");
  } else {
    htmlClassList.remove("dark-theme");
    htmlClassList.add("light-theme");
  }
});

/*СКРИПТ ДЛЯ КОНФИГУРАТОРА */
const brandsSelect = document.getElementById('brand');
const modelsSelect = document.getElementById('model');
const colorSelect = document.getElementById('color');
const priceInput = document.getElementById('price');
const buyBtn = document.getElementById('buy-btn');

const carData = {
    bmw: {
        '3-series': 40000,
        '5-series': 60000,
        '7-series': 100000,
    },
    audi: {
        'A4': 35000,
        'A6': 55000,
        'A8': 90000,
    },
    mercedes: {
        'C-class': 45000,
        'E-class': 65000,
        'S-class': 110000,
    },
};

brandsSelect.addEventListener('change', function() {
    modelsSelect.innerHTML = '<option value="">Выбрать</option>';
    if (this.value) {
        const models = Object.keys(carData[this.value]);
        models.forEach(function(model) {
            modelsSelect.innerHTML += `<option value="${model}">${model}</option>`;
        });
    }
});

modelsSelect.addEventListener('change', function() {
    priceInput.value = '';
    if (brandsSelect.value && this.value) {
        const price = carData[brandsSelect.value][this.value];
        priceInput.value = `$${price}`;
    }
});

colorSelect.addEventListener('change', function() {
    if (!priceInput.value) {
        priceInput.value = 'Выбрать';
    }
});

/* ДЛЯ SVG*/
document.getElementById('buy-btn').addEventListener('click', function() {
    document.getElementById('popup').style.display = 'block';
    document.getElementById('carsvg').style.animation = 'spin 1s linear infinite';
    document.getElementById('message').style.display = 'block';
  });