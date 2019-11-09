from StringHelper import StringHelper;
from BMFontReader import BMFontReader;
import os, sys, csv;

reload(sys) 
sys.setdefaultencoding('utf8')

def gen_gms_font():
	# read text
	f = open("minit_loc.csv", "rb");
	csv_reader = csv.reader(f, delimiter=";");
	
	txts = "";
	for row in csv_reader:
		txts += (row[11] + row[12]);
	f.close();

	# min text
	sh = StringHelper();
	sh.add_chars(txts.decode("utf-8"));
	sh.add_western();
	f = open("Font/textmin.txt", "wb");
	f.write(sh.get_chars().decode("utf-8").encode("utf-8-sig"));
	f.close();

	# Can't add " ", make sure the path have no space.
	bmfc_filepath = "Font/fntChineseTest.bmfc";
	output_filepath = "Font/fntChineseTest.fnt";
	
	bmfont_tool_path = "E:\\BMFont\\bmfont.com";
	text_file_path = "\"Font\\textmin.txt\"";
	bmfc_filepath = "\"" + bmfc_filepath.replace("/", "\\") + "\"";
	output_filepath = "\"" + output_filepath.replace("/", "\\") + "\"";
	commandstr = " ".join((bmfont_tool_path , "-c" ,bmfc_filepath, "-o", output_filepath, "-t" ,text_file_path));
	os.system(commandstr.encode('mbcs'));

def gen_gms_fon_mapping():
	bm_reader = BMFontReader("Font/fntChineseTest.fnt");
	
	f = open("Font/fntChineseTest.csv", "wb");
	csv_writer = csv.writer(f, delimiter=";");

	for glyph in bm_reader.glyphs:
		csv_writer.writerow([glyph["id"], glyph["x"], glyph["y"], glyph["width"], glyph["height"], glyph["xadvance"], glyph["xoffset"]]);
	f.close();
	
gen_gms_font();
gen_gms_fon_mapping();