Feature: Actualizar vehículo

  Scenario: Generar un reporte
    Given Se inicia el navegador
    When Entra a la seccion reporte
    And Llenar el campo ID Viaje 125
    And Aplastar el boton para buscar
    Then Visualizar reporte viaje

  Scenario: Ingresar una id de viaje incorrecto
    Given Se inicia el navegador
    When Entra a la seccion reporte
    And Llenar el campo ID Viaje 111
    And Aplastar el boton para buscar
    Then Visualizar reporte viaje
