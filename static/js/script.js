// Erstellen eines Arrays und Übergeben der Nummer, Fragen, Optionen und Antworten
var questions = [];

fetch("/quiz-questions")
  .then((response) => response.json())
  .then((data) => {
    questions = data;
    console.log(questions);
  });

// Auswahl aller erforderlichen Elemente
const start_btn = document.querySelector(".start_btn button");
const info_box = document.querySelector(".info_box");
const explanation_text = document.querySelector(".explanation_text");
const exit_btn = info_box.querySelector(".buttons .quit");
const continue_btn = info_box.querySelector(".buttons .restart");
const quiz_box = document.querySelector(".quiz_box");
const result_box = document.querySelector(".result_box");
const option_list = document.querySelector(".option_list");
const time_line = document.querySelector("header .time_line");
const timeText = document.querySelector(".timer .time_left_txt");
const timeCount = document.querySelector(".timer .timer_sec");

// Wenn der Start-Quiz-Button geklickt wird
start_btn.onclick = () => {
  info_box.classList.add("activeInfo"); // Info-Box anzeigen
};

// Wenn der Exit-Quiz-Button geklickt wird
exit_btn.onclick = () => {
  info_box.classList.remove("activeInfo"); // Info-Box ausblenden
  console.log('Quit-Button geklickt.')
  window.location.href = "/"
};

// Wenn der Continue-Quiz-Button geklickt wird
continue_btn.onclick = () => {
  info_box.classList.remove("activeInfo"); // Info-Box ausblenden
  quiz_box.classList.add("activeQuiz"); // Quiz-Box anzeigen
  showQuetions(0); // Aufrufen der showQestions-Funktion
  queCounter(1); // Übergabe von 1 Parameter an queCounter
  startTimer(15); // Aufrufen der startTimer-Funktion
  startTimerLine(0); // Aufrufen der startTimerLine-Funktion
};

let timeValue = 15;
let que_count = 0;
let que_numb = 1;
let userScore = 0;
let counter;
let counterLine;
let widthValue = 0;

const restart_quiz = result_box.querySelector(".buttons .restart");
const quit_quiz = result_box.querySelector(".buttons .quit");

// Wenn der Restart-Quiz-Button geklickt wird
restart_quiz.onclick = () => {
  quiz_box.classList.add("activeQuiz"); // Quiz-Box anzeigen
  result_box.classList.remove("activeResult"); // Ergebnis-Box ausblenden
  timeValue = 15;
  que_count = 0;
  que_numb = 1;
  userScore = 0;
  widthValue = 0;
  showQuetions(que_count); // Aufrufen der showQestions-Funktion
  queCounter(que_numb); // Übergabe des que_numb-Werts an queCounter
  clearInterval(counter); // Zähler zurücksetzen
  clearInterval(counterLine); // ZählerLine zurücksetzen
  startTimer(timeValue); // Aufrufen der startTimer-Funktion
  startTimerLine(widthValue); // Aufrufen der startTimerLine-Funktion
  timeText.textContent = "Verbleibende Zeit"; // Text von timeText auf Verbleibende Zeit ändern
  next_btn.classList.remove("show"); // Nächster Button ausblenden
};

// Wenn der Quit-Quiz-Button geklickt wird
quit_quiz.onclick = () => {
    console.log('Letzter Quiz-Button')
//   window.location.reload(); // Aktuelles Fenster neu laden
    window.location.href = "/"
};

const next_btn = document.querySelector("footer .next_btn");
const bottom_ques_counter = document.querySelector("footer .total_que");

// Wenn der Next-Que-Button geklickt wird
next_btn.onclick = () => {
  if (que_count < questions.length - 1) {
    // Wenn die Frageanzahl kleiner ist als die Gesamtanzahl der Fragen
    que_count++; // Erhöhe den que_count-Wert
    que_numb++; // Erhöhe den que_numb-Wert
    showQuetions(que_count); // Aufrufen der showQestions-Funktion
    queCounter(que_numb); // Übergabe des que_numb-Werts an queCounter
    clearInterval(counter); // Zähler zurücksetzen
    clearInterval(counterLine); // ZählerLine zurücksetzen
    startTimer(timeValue); // Aufrufen der startTimer-Funktion
    startTimerLine(widthValue); // Aufrufen der startTimerLine-Funktion
    timeText.textContent = "Verbleibende Zeit"; // Text von timeText auf Verbleibende Zeit ändern
    next_btn.classList.remove("show"); // Nächster Button ausblenden
  } else {
    clearInterval(counter); // Zähler zurücksetzen
    clearInterval(counterLine); // ZählerLine zurücksetzen
    showResult(); // Aufrufen der showResult-Funktion
  }
};

// Holen von Fragen und Optionen aus dem Array
function showQuetions(index) {
  const que_text = document.querySelector(".que_text");
  explanation_text.innerHTML = "";
  // Erstellen einer neuen span- und div-Tags für Frage und Option und Übergeben des Werts mithilfe des Array-Index
  let que_tag =
    "<span>" +
    questions[index].numb +
    ". " +
    questions[index].question +
    "</span>";
  let option_tag =
    '<div class="option"><span>' +
    questions[index].options[0] +
    "</span></div>" +
    '<div class="option"><span>' +
    questions[index].options[1] +
    "</span></div>" +
    '<div class="option"><span>' +
    questions[index].options[2] +
    "</span></div>";
  que_text.innerHTML = que_tag; // Neues span-Tag innerhalb von que_tag hinzufügen
  option_list.innerHTML = option_tag; // Neues div-Tag innerhalb von option_tag hinzufügen

  const option = option_list.querySelectorAll(".option");

  // Setzen des onclick-Attributs für alle verfügbaren Optionen
  for (i = 0; i < option.length; i++) {
    option[i].setAttribute("onclick", "optionSelected(this)");
  }
}
// Erstellen der neuen div-Tags für Symbole
let tickIconTag = '<div class="icon tick"><i class="fas fa-check"></i></div>';
let crossIconTag = '<div class="icon cross"><i class="fas fa-times"></i></div>';

// Wenn der Benutzer auf eine Option klickt
function optionSelected(answer) {
  clearInterval(counter); // Zähler zurücksetzen
  clearInterval(counterLine); // ZählerLine zurücksetzen
  let userAns = answer.textContent; // Auswahl der vom Benutzer ausgewählten Option
  let correcAns = questions[que_count].answer; // Auswahl der korrekten Antwort aus dem Array
  const allOptions = option_list.children.length; // Auswahl aller Optionsitems

  if (userAns == correcAns) {
    // Wenn die vom Benutzer ausgewählte Option der korrekten Antwort des Arrays entspricht
    userScore += 1; // Erhöhen des Punktwerts um 1
    answer.classList.add("correct"); // Hinzufügen von grüner Farbe zur korrekt ausgewählten Option
    answer.insertAdjacentHTML("beforeend", tickIconTag); // Hinzufügen des Hakenymbols zur korrekt ausgewählten Option
    console.log("Richtige Antwort");
    console.log("Ihre richtigen Antworten = " + userScore);
  } else {
    answer.classList.add("incorrect"); // Hinzufügen von roter Farbe zur korrekt ausgewählten Option
    answer.insertAdjacentHTML("beforeend", crossIconTag); // Hinzufügen des Kreuzsymbols zur korrekt ausgewählten Option
    console.log("Falsche Antwort");
    explanation_text.innerHTML = `Erklärung: <br>${questions[que_count].explanation}`;

    for (i = 0; i < allOptions; i++) {
      if (option_list.children[i].textContent == correcAns) {
        // Wenn es eine Option gibt, die mit einer Array-Antwort übereinstimmt
        option_list.children[i].setAttribute("class", "option correct"); // Hinzufügen von grüner Farbe zur übereinstimmenden Option
        option_list.children[i].insertAdjacentHTML("beforeend", tickIconTag); // Hinzufügen des Hakenymbols zur übereinstimmenden Option
        console.log("Automatisch ausgewählte richtige Antwort.");
      }
    }
  }
  for (i = 0; i < allOptions; i++) {
    option_list.children[i].classList.add("disabled"); // Sobald der Benutzer eine Option auswählt, werden alle Optionen deaktiviert
  }
  next_btn.classList.add("show"); // Nächster Button anzeigen, wenn der Benutzer eine Option auswählt
}

function showResult() {
  info_box.classList.remove("activeInfo"); // Info-Box ausblenden
  quiz_box.classList.remove("activeQuiz"); // Quiz-Box ausblenden
  result_box.classList.add("activeResult"); // Ergebnis-Box anzeigen
  const scoreText = result_box.querySelector(".score_text");
  if (userScore > 3) {
    // Wenn der Benutzer mehr als 3 Punkte erzielt hat
    // Erstellen eines neuen span-Tags und Übergeben der Benotung und der Gesamtanzahl der Fragen
    let scoreTag =
      "<span>und Glückwunsch! 🎉, Sie haben <p>" +
      userScore +
      "</p> von <p>" +
      questions.length +
      "</p></span>";
    scoreText.innerHTML = scoreTag; // Neues span-Tag innerhalb von score_Text hinzufügen
  } else if (userScore > 1) {
    // Wenn der Benutzer mehr als 1 Punkt erzielt hat
    let scoreTag =
      "<span>und nett 😎, Sie haben <p>" +
      userScore +
      "</p> von <p>" +
      questions.length +
      "</p></span>";
    scoreText.innerHTML = scoreTag;
  } else {
    // Wenn der Benutzer weniger als 1 Punkt erzielt hat
    let scoreTag =
      "<span>und sorry 😐, Sie haben nur <p>" +
      userScore +
      "</p> von <p>" +
      questions.length +
      "</p></span>";
    scoreText.innerHTML = scoreTag;
  }

  const data = {
    score: userScore,
  };

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json", // Setzen des geeigneten Inhalts für Ihre Anfrage
      // Hinzufügen von zusätzlichen Headern bei Bedarf
    },
    body: JSON.stringify(data), // Umwandeln der Daten in das JSON-Format
  };

  fetch("/update_marks", options)
    .then((response) => response.json()) // Angenommen, der Server gibt JSON zurück
    .then((data) => {
      // Verarbeiten der Antwortdaten
      console.log("Antwort:", data);
    })
    .catch((error) => {
      // Fehler behandeln
      console.error("Fehler:", error);
    });
}

function startTimer(time) {
  counter = setInterval(timer, 1000);
  function timer() {
    timeCount.textContent = time; // Ändern des Werts von timeCount mit dem Zeitwert
    time--; // Dekrementieren des Zeitwerts
    if (time < 9) {
      // Wenn der Timer kleiner als 9 ist
      let addZero = timeCount.textContent;
      timeCount.textContent = "0" + addZero; // Hinzufügen einer 0 vor dem Zeitwert
    }
    if (time < 0) {
      // Wenn der Timer kleiner als 0 ist
      clearInterval(counter); // Zähler zurücksetzen
      timeText.textContent = "Zeit abgelaufen"; // Ändern des Textes von timeText auf Zeit abgelaufen
      const allOptions = option_list.children.length; // Auswahl aller Optionsitems
      let correcAns = questions[que_count].answer; // Auswahl der korrekten Antwort aus dem Array
      for (i = 0; i < allOptions; i++) {
        if (option_list.children[i].textContent == correcAns) {
          // Wenn es eine Option gibt, die mit einer Array-Antwort übereinstimmt
          option_list.children[i].setAttribute("class", "option correct"); // Hinzufügen von grüner Farbe zur übereinstimmenden Option
          option_list.children[i].insertAdjacentHTML("beforeend", tickIconTag); // Hinzufügen des Hakenymbols zur übereinstimmenden Option
          console.log("Zeit abgelaufen: Automatisch ausgewählte richtige Antwort.");
        }
      }
      for (i = 0; i < allOptions; i++) {
        option_list.children[i].classList.add("disabled"); // Sobald der Benutzer eine Option auswählt, werden alle Optionen deaktiviert
      }
      next_btn.classList.add("show"); // Nächster Button anzeigen, wenn der Benutzer eine Option auswählt
    }
  }
}

function startTimerLine(time) {
  counterLine = setInterval(timer, 29);
  function timer() {
    time += 1; // Erhöhen des Zeitwerts um 1
    time_line.style.width = time + "px"; // Erhöhen der Breite von time_line um px um den Zeitwert
    if (time > 549) {
      // Wenn der Zeitwert größer als 549 ist
      clearInterval(counterLine); // ZählerLine zurücksetzen
    }
  }
}
// Funktion für die Anzeige der Fragezähler
function queCounter(index) {
  // Erstellen eines neuen span-Tags und Übergeben der Fragennummer und der Gesamtanzahl der Fragen
  let totalQueCounTag =
    "<span><p>" +
    index +
    "</p> von <p>" +
    questions.length +
    "</p> Fragen</span>";
  bottom_ques_counter.innerHTML = totalQueCounTag; // Neues span-Tag innerhalb von bottom_ques_counter hinzufügen
}
