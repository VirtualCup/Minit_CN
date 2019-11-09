using UndertaleModLib.Util;

UndertaleFont font = Data.Fonts.ByName("fntChineseTest");
using(StreamReader reader = new StreamReader("fntChineseTest.csv"))
{
	font.Glyphs.Clear();
	string line;
	while((line = reader.ReadLine()) != null)
	{
		string[] s = line.Split(';');
		font.Glyphs.Add(new UndertaleFont.Glyph() {
			Character = UInt16.Parse(s[0]),
			SourceX = UInt16.Parse(s[1]),
			SourceY = UInt16.Parse(s[2]),
			SourceWidth = UInt16.Parse(s[3]),
			SourceHeight = UInt16.Parse(s[4]),
			Shift = Int16.Parse(s[5]),
			Offset = Int16.Parse(s[6]),
		});
	}
	
	font.Texture.SourceWidth = 1024;
	font.Texture.SourceHeight = 1024;
	font.Texture.TargetWidth = 1024;
	font.Texture.TargetHeight = 1024;
	font.Texture.BoundingWidth = 1024;
	font.Texture.BoundingHeight = 1024;
	
	font.Texture.TexturePage.TextureData.TextureBlob = TextureWorker.ReadTextureBlob("fntChineseTest_0.png");
	
}