<?php
    $servername = "localhost";
    $username = "root";
    $password = "Franio2007!#";
    $dbname = "monitory";

    // Połączenie z bazą danych
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Sprawdzenie połączenia
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Obsługa formularza
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $response = $_POST['response'];

        // Wstawienie odpowiedzi do bazy danych
        $sql = "INSERT INTO valentine_responses (response) VALUES ('$response')";

        if ($conn->query($sql) === TRUE) {
            echo "Dziękuję! Odpowiedź została zapisana w bazie danych.";
        } else {
            echo "Błąd: " . $sql . "<br>" . $conn->error;
        }
    }

    // Zamknięcie połączenia z bazą danych
    $conn->close();
    ?>