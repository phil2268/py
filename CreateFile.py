"""
def search_asset_num(conn, assetNum):
    cur = conn.cursor()
    cur.execute("SELECT * FROM assets WHERE AssetNumber = ?", (assetNum,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
      
cur.execute("SELECT "+column+" FROM Data where "+goal+"=?", (constrain,))       
"""        
column = "commands"
goal = "id='1' "
constrain = "DESC"       
cur = "SELECT "+column+" FROM Data where "+goal+"=?", (constrain,)

print(cur)
