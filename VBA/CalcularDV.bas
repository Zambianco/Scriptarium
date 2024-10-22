Attribute VB_Name = "Módulo1"
' Script para calcular o dígito verificador usando mod 11
' Autor: Veloster
' Data: 2023-06-06

Function CalcularDV(numero As String) As Integer
    Dim pesos() As Variant
    Dim digitoVerificador As Integer
    Dim resto As Integer

    ' Define os pesos usados no cálculo
    pesos = Array(2, 3, 4, 5, 6, 7, 8, 9)

    Dim i As Integer
    Dim soma As Integer
    soma = 0

    ' Calcula a soma ponderada dos dígitos do número
    For i = Len(numero) To 1 Step -1
        Dim digito As Integer
        digito = CInt(Mid(numero, i, 1)) ' Obtém o dígito na posição i

        ' Acumula a soma com base nos pesos
        soma = soma + (digito * pesos((Len(numero) - i) Mod 8))
    Next i

    ' Calcula o resto da divisão da soma por 11
    resto = soma Mod 11
    
    ' Inicializa o dígito verificador
    digitoVerificador = 11 - resto
    
    ' Ajusta o dígito verificador se maior que 9
    If digitoVerificador > 9 Then
        digitoVerificador = 0
    End If
    
    ' Retorna o dígito verificador
    CalcularDV = digitoVerificador
End Function
