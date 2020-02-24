import React from "react"
import { graphql, useStaticQuery, Link } from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"

const IndexPage = () => {

  const data = useStaticQuery(graphql`
      query {
        allRestApiServicios {
          edges {
            node {
              id
              estado
              descripcion
              moto {
                patente
                cliente {
                  nombre
                  apellido
                }
              }
            }
          }
        }
      }`);

  return (
    <div>
      <SEO title="Home"/>
      <h1>Hi people</h1>
      <p>Welcome to your new Gatsby site.</p>
      <p>Now go build something great.</p>
      <div style={{ maxWidth: `300px`, marginBottom: `1.45rem` }}>
        <Image />
      </div>
          <tr>
            <td><span>id</span></td>
            <td><span>estado</span></td>
            <td><span>descripcion</span></td>
            <td><span>patente</span></td>
            <td><span>nombre cliente</span></td>
            <td><span>apellido cliente</span></td>
          </tr>
      {data.allRestApiServicios.edges.map(edge => {
        return (
          <tr>
            <td>{edge.node.id}</td>
            <td>{edge.node.estado}</td>
            <td>{edge.node.descripcion}</td>
            <td>{edge.node.moto.patente}</td>
            <td>{edge.node.moto.cliente.nombre}</td>
            <td>{edge.node.moto.cliente.apellido}</td>
          </tr>
        );
      })}
      <Link to="/page-2/">Go to page 2</Link>
    </div>
  )
}

export default IndexPage
