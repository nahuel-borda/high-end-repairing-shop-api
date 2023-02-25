import React from "react"
import { graphql, useStaticQuery, Link } from "gatsby"
import { FaAngleDoubleRight} from 'react-icons/fa';

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"

import '../components/dashboard.css';

const IndexPage = () => {

  const data = useStaticQuery(graphql`
      query {
        allRestApiServices {
          edges {
            node {
              id
              estado
              descripcion
              device {
                patente
                model {
                  name
                }
                brand {
                  name
                }
                client {
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
      <div id="dashboard">
        <div id="dashboard_header">
          <div id="header_title"><h1>Integral Devices</h1></div>
          <div id='header_logo'><div id="logo_image"><Image/></div></div>
        </div>
        <div class="en_espera_board board">
          <h1>En Espera</h1>
          <span class="ncards"></span>
          <div class="cardwrappper">
          {data.allRestApiServices.edges.map(edge => {
            if (edge.node.estado === 'En espera') {
              return (
                <div class="card">
                  <h1>{edge.node.device.brand.name} {edge.node.device.model.name}</h1>
                  <div class="descripcion">
                    <div class="descripcion-text">
                      <span>{edge.node.descripcion}</span>
                    </div>
                  </div>
                  <span>Vehiculo: {edge.node.device.patente}</span>
                  <div class="estado_wrapper">
                    <div class="estado_card">
                      <span class="estado_card_text">
                        <span class='estado_value'>{edge.node.estado}</span>
                      </span>
                    </div>
                    <div class="card_buttons">
                      <button class="take_card_button"><span><FaAngleDoubleRight/></span></button>
                    </div>
                  </div>
                </div>
              );
            }
          })}
          </div>
        </div>
        <div class="en_proceso_board board">
          <h1>En Proceso</h1>
          <span class="ncards"></span>
          <div class="cardwrappper">
          {data.allRestApiServices.edges.map(edge => {
            if (edge.node.estado === 'En proceso') {
              return (
                <div class="card">
                  <h1>{edge.node.device.brand.name} {edge.node.device.model.name}</h1>
                  <div class="descripcion">
                    <div class="descripcion-text">
                      <span></span>
                    </div>
                  </div>
                  <span>Vehiculo: {edge.node.device.patente}</span>
                  <div class="estado_wrapper">
                    <div class="estado_card">
                      <span class="estado_card_text">
                        <span class='estado_value'>{edge.node.estado}</span>
                      </span>
                    </div>
                  </div>
                </div>
              );
            }
          })}
          </div>
        </div>
        <div class="finalizado_board board">
          <h1>Finalizado</h1>
          <span class="ncards"></span>
          <div class="cardwrappper">
          {data.allRestApiServices.edges.map(edge => {
            if (edge.node.estado === 'Finalizado') {
              return (
                <div class="card">
                  <h1>{edge.node.device.brand.name} {edge.node.device.model.name}</h1>
                  <div class="descripcion">
                    <div class="descripcion-text">
                      <span></span>
                    </div>
                  </div>
                  <span>Vehiculo: {edge.node.device.patente}</span>
                  <div class="estado_wrapper">
                    <div class="estado_card">
                      <span class="estado_card_text">
                        <span class='estado_value'>{edge.node.estado}</span>
                      </span>
                    </div>
                  </div>
                </div>
              );
            }
          })}
          </div>
        </div>
        <div class="demorado_board board">
          <h1>Demorado</h1>
          <span class="ncards"></span>
          <div class="cardwrappper">
          {data.allRestApiServices.edges.map(edge => {
            if (edge.node.estado === 'Demorado') {
              return (
                <div class="card">
                  <h1>{edge.node.device.brand.name} {edge.node.device.model.name}</h1>
                  <div class="descripcion">
                    <div class="descripcion-text">
                      <span>{edge.node.descripcion}</span>
                    </div>
                  </div>
                  <span>Vehiculo: {edge.node.device.patente}</span>
                  <div class="estado_wrapper">
                    <div class="estado_card">
                      <span class="estado_card_text">
                        <span class='estado_value'>{edge.node.estado}</span>
                      </span>
                    </div>
                  </div>
                </div>
              );
            }
          })}
          </div>
        </div>
      </div>        
    </div>
  )
}

export default IndexPage
