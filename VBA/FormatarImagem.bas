Attribute VB_Name = "NewMacros"
Sub FormatarImagemRAF()
    Selection.Paste
    Selection.MoveRight Unit:=wdCharacter, Count:=1, Extend:=wdExtend
    
    ' Redimensionar a imagem
    With Selection.InlineShapes(1)
        .Height = CentimetersToPoints(5.85)
        .Width = CentimetersToPoints(7.8)
    End With
    
    ' Adicionar borda preta de 1pt
    With Selection.InlineShapes(1).Line
        .Weight = wdLineWidth2pt
        .ForeColor.RGB = RGB(0, 0, 0) ' Cor preta
    End With
    
    ' Adicionar espaçamento antes e depois da imagem em pontos (pt)
    With Selection.ParagraphFormat
        .SpaceBefore = 3 ' 3,0 pt antes
        .SpaceAfter = 3 ' 3,0 pt depois
    End With
End Sub
