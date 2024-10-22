Attribute VB_Name = "Funcao_CONCATIF"
Option Explicit

' Função que concatena valores de uma faixa com base em um critério de busca.
Function CONCATIF(LookupRange As Range, LookupVal As Variant, ConcatRange As Range, Optional Separator As String = vbNewLine) As Variant

    Dim i As Integer
    Dim Result As String

    On Error Resume Next ' Ignora erros durante a execução

    ' Verifica se LookupRange e ConcatRange têm o mesmo número de células
    If LookupRange.Count <> ConcatRange.Count Then
        CONCATIF = CVErr(xlErrRef) ' Retorna erro se as faixas não forem compatíveis
        Exit Function
    End If

    ' Percorre cada célula na faixa de busca
    For i = 1 To LookupRange.Count
        ' Se o valor da célula corresponder ao valor de busca
        If LookupRange.Cells(i).Value = LookupVal Then
            Result = Result & Separator & ConcatRange.Cells(i).Value ' Concatena o valor
        End If
    Next i

    ' Remove o separador inicial, se houver resultados
    If Result <> "" Then
        Result = VBA.Mid(Result, VBA.Len(Separator) + 1)
    End If

    CONCATIF = Result ' Retorna o resultado final

End Function

Sub Lookup_and_Concat()
    ' Sub ainda não implementada, pode ser usada para integrar a função CONCATIF.
End Sub
