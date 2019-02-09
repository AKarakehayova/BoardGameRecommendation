
import React from 'react'
import ReactTable from "react-table";
import data from '../classification.json'
export class App extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
    }
  }

  

  render () {
    
    return (<div>
               <ReactTable
          data={data}
          columns={[
            {
              columns: [
                {
                  Header: "Name",
                  accessor: "name"
                }
              ]
            },
            {
              columns: [
                {
                  Header: "Count",
                  accessor: "count"
                }
              ]
            },
            {
              columns: [
                {
                  Header: "Polarity",
                  accessor: "polarity"
                }
              ]
            },
            {
              columns: [
                {
                  Header: "Subjectivity",
                  accessor: "subjectivity"
                }
              ]
            },
            {
              columns: [
                {
                  Header: "Keywords",
                  id: "keywords",
                  accessor: data => data.keywords.join(", ")
                }
              ]
            }
          ]}
          showPagination ={false} 
          className="-striped -highlight"
        />
    </div >)
  }
}

export default App
