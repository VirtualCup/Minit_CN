UndertaleFont font = Data.Fonts.ByName("fntChineseTest");
using(StreamWriter writer = new StreamWriter("fntChineseTest.old.csv"))
{
	writer.WriteLine("charID;" + "x;" + "y;" + "width;" + "height;" + "shift;" + "offset");
	foreach(var g in font.Glyphs)
	{
		writer.WriteLine(g.Character+";"+g.SourceX+";"+g.SourceY+";"+g.SourceWidth+";"+g.SourceHeight+";"+g.Shift+";"+g.Offset);
	}
}