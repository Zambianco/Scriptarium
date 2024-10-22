Sub Mesclar_horizontal()
    ' Esta macro mescla células selecionadas horizontalmente em uma tabela do Word.
    
    Selection.MoveRight Unit:=wdCharacter, Count:=2, Extend:=wdExtend ' Seleciona duas células à direita
    Selection.Cells.Merge ' Mescla as células selecionadas
    Selection.MoveLeft Unit:=wdCharacter, Count:=1 ' Move o cursor de volta uma posição
End Sub
