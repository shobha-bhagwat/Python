import unicodecsv
import xlrd
import datetime
import os

def excel2csv (excel_file, csv_file):
    workbook = xlrd.open_workbook(excel_file)
    all_worksheets = workbook.sheet_names()
    fh = open(csv_file,"wb")
    csv_out = unicodecsv.writer(fh, encoding='utf-8')

    for worksheet_name in all_worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)

        for rownum in xrange(worksheet.nrows):
            rowData = []
            for colnum in xrange(worksheet.ncols):
                cell = worksheet.cell(rownum, colnum)   #get individual cell
                if cell.ctype == xlrd.XL_CELL_DATE:
                    dt_tuple = xlrd.xldate_as_tuple(cell.value, workbook.datemode)    # Create datetime object from this tuple.
                    get_col = datetime.datetime(
                        dt_tuple[0], dt_tuple[1], dt_tuple[2],
                        dt_tuple[3], dt_tuple[4], dt_tuple[5]
                    )
                elif cell.ctype == xlrd.XL_CELL_NUMBER:
                    get_col = int(cell.value)
                else:
                    get_col = unicode(cell.value)
                rowData.append(get_col)
            csv_out.writerow(rowData)


excel_file = 'filename.xlsx'
csv_file = 'filename.csv'

if os.path.exists(csv_file):
    os.remove(csv_file)
    print("Deleted file")


excel2csv(excel_file, csv_file)
