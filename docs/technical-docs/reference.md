---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label}
Abinesh Gulasingam

{: .label. label-green }
Sebastian Lukas Nieme

# Reference documentation
{: .no_toc }


<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## home()

**Route:** `/`

**Methoden:** `GET`

**Zweck:** Zeigt die Startseite der Anwendung an.

---

## login()

**Route:** `/login`

**Methoden:** `GET`, `POST`

**Zweck:** Erlaubt Benutzern das Einloggen in die Anwendung.

---

## register()

**Route:** `/register`

**Methoden:** `GET`, `POST`

**Zweck:** Erlaubt Benutzern die Registrierung für einen neuen Account in der Anwendung.

---

## select_difficulty()

**Route:** `/select_difficulty`

**Methoden:** `GET`, `POST`

**Zweck:** Erlaubt Benutzern die Auswahl der Schwierigkeitsstufe für das Quiz.

---

## quiz()

**Route:** `/quiz`

**Methoden:** `GET`, `POST`

**Zweck:** Zeigt das Quiz an.

---

## quiz_questions()

**Route:** `/quiz-questions`

**Methoden:** `GET`

**Zweck:** Gibt die Fragen des Quiz zurück, basierend auf der ausgewählten Schwierigkeitsstufe.

---

## update_marks()

**Route:** `/update_marks`

**Methoden:** `POST`

**Zweck:** Aktualisiert die Punktzahl des Benutzers nach Abschluss des Quiz.

---

## quiz_high_score_result() 

**Route:** `/quiz/high-score`

**Methoden:** `GET`

**Zweck:** Zeigt die Bestenliste der Benutzer mit den höchsten Punktzahlen an.

---

## reset_quiz()

**Route:** `/resetQuiz`

**Methoden:** `GET`

**Zweck:** Setzt die Auswahl der Schwierigkeitsstufe für das Quiz zurück.

---

## profile()

**Route:** `/profile`

**Methoden:** `GET`

**Zweck:** Zeigt das Benutzerprofil an.

---

## logout()

**Route:** `/logout`

**Methoden:** `GET`

**Zweck:** Erlaubt Benutzern das Ausloggen aus der Anwendung.

