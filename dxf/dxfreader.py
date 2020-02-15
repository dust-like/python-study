import shutil
import turtle as tt

dxf_filename = 'dxf_files/file.dxf'
txt_filename = 'txt_files/file.txt'

shutil.copyfile(dxf_filename,txt_filename)

a = 0	#标识符
h = []
with open(txt_filename, encoding="utf-8") as file_object:
	for line in file_object:
		if line.strip() == 'ENTITIES':
			a = 1
		if a == 1:
			h.append(line.strip())
		if a == 1 and line.strip() == 'ENDSEC':
			a = 0
print(h)	#提取实体段
i = len(h)	#测量列表长度
print(i)
rate = float(input())
j = 0
tt.speed(0)
tt.Turtle().screen.delay(0)
for p in h:
	j = j + 1
	if p == 'AcDbLine':		#找到线起点端点
		c = ['','','','']
		c[0] = float(h[j+1])*rate
		c[1] = float(h[j+3])*rate
		c[2] = float(h[j+7])*rate
		c[3] = float(h[j+9])*rate
		print(c)
		tt.up()
		tt.goto(c[0],c[1])
		tt.down()
		tt.goto(c[2],c[3])
		tt.up()
	if p == 'AcDbCircle':
		c = ['','','']
		c[0] = float(h[j+1])*rate
		c[1] = float(h[j+3])*rate
		c[2] = float(h[j+7])*rate
		print(c)
		tt.up()
		tt.goto(c[0],c[1])
		tt.down()
		tt.circle(c[2])
		tt.up()
tt.done()
