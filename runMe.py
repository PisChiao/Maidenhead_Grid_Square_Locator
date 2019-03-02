import posToGrid

if __name__ == "__main__":
    lon = 0
    lat = 0
    while True:        
        print('请输入经度，以小数表示，西经为负数。')
        print('例如：西经23°27′30″，应输入为-23.45833')
        lon = input('请输入经度：').strip()
        try:
            lon = float(lon)
            if lon >= -180 and lon <= 180:
                break
            else:
                print('经度只能介于-180到180之间！\n')
                continue
        except:
            print('只能输入数字！\n')        

    while True:
        print('请输入纬度，以小数表示，南纬为负数。')
        print('例如：南纬23°27′30″，应输入为-23.45833')
        lat = input('请输入纬度：')
        try:
            lat = float(lat)
            if lat >= -90 and lat <= 90:
                break
            else:
                print('纬度只能介于-90到90之间！\n')
                continue
        except:
            print('只能输入数字！\n')

    print('\n您查询的地点所述梅登海格坐标为：' + posToGrid.getGrid(lon,lat))
    print('DE BI7JAC TNX 73')