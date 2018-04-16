#Google App Script
function moveValuesMine(){
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  var prevWriteSource = ss.getRange('SheetTabOutput!C160');
  
  
  var prevX   = prevWriteSource.getCell(1, 1).getValue(); // write to 4 cell at yesterday.

  var todayX  = prevX + 1; // write to 5 at today.
  Logger.log(todayX);
  
  var endDay = 108;
  
  if (todayX < endDay){
  
  var source = ss.getRange('SheetTabTarget!B12');
  var range=ss.getRange('SheetTabOutput!E5:FC5');

  var session = source.getCell(1, 1).getValue(); 
  range.getCell(1, todayX).setValue(session);

  prevWriteSource.getCell(1, 1).setValue(todayX); 
  }
}
