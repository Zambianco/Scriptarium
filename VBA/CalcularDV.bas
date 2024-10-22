Attribute VB_Name = "M�dulo1"
' Script para calcular o d�gito verificador usando mod 11
' Autor: Veloster
' Data: 2023-06-06

Function CalcularDV(numero As String) As Integer
    Dim pesos() As Variant
    Dim digitoVerificador As Integer
    Dim resto As Integer

    ' Define os pesos usados no c�lculo
    pesos = Array(2, 3, 4, 5, 6, 7, 8, 9)

    Dim i As Integer
    Dim soma As Integer
    soma = 0

    ' Calcula a soma ponderada dos d�gitos do n�mero
    For i = Len(numero) To 1 Step -1
        Dim digito As Integer
        digito = CInt(Mid(numero, i, 1)) ' Obt�m o d�gito na posi��o i

        ' Acumula a soma com base nos pesos
        soma = soma + (digito * pesos((Len(numero) - i) Mod 8))
    Next i

    ' Calcula o resto da divis�o da soma por 11
    resto = soma Mod 11
    
    ' Inicializa o d�gito verificador
    digitoVerificador = 11 - resto
    
    ' Ajusta o d�gito verificador se maior que 9
    If digitoVerificador > 9 Then
        digitoVerificador = 0
    End If
    
    ' Retorna o d�gito verificador
    CalcularDV = digitoVerificador
End Function
