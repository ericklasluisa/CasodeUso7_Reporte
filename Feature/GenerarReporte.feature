Feature: Generar Reporte

  Scenario: Generar un reporte
    Given Se inicia el navegador generar reporte
    When Entra a la seccion reporte
    And Llenar en reporte el campo ID Viaje 125
    And Aplastar el boton para buscar reporte
    Then Visualizar reporte viaje

  Scenario: Ingresar una id de viaje incorrecto
    Given Se inicia el navegador generar reporte
    When Entra a la seccion reporte
    And Llenar en reporte el campo ID Viaje 111
    And Aplastar el boton para buscar reporte
    Then Visualizar reporte viaje
