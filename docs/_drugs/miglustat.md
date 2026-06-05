---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Miglustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Miglustat: De Enfermedad de Gaucher Tipo 1 a Enfermedad de Tay-Sachs

## Resumen en Una Frase

Miglustat (Zavesca®) es un inhibidor oral de glucosilceramida sintasa (GCS) aprobado internacionalmente para la enfermedad de Gaucher tipo 1, en la que reduce la acumulación de glucosilceramida mediante terapia de reducción de sustrato (SRT).
El modelo TxGNN predice que podría ser efectivo para la **Enfermedad de Tay-Sachs**, con **5 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
La solidez mecanística es alta: el GM2 que se acumula en Tay-Sachs se sintetiza a través de glucosilceramida, el mismo precursor que Miglustat reduce en el punto de acción de GCS.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Gaucher tipo 1 (aprobación internacional; sin registro en Colombia) |
| Nueva Indicación Predicha | Enfermedad de Tay-Sachs |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Miglustat actúa inhibiendo glucosilceramida sintasa (GCS), la enzima que cataliza la formación de glucosilceramida a partir de ceramida y UDP-glucosa. Al reducir la síntesis de glucosilceramida, disminuye el sustrato disponible para la producción de glucoesfingolípidos complejos. Este mecanismo de terapia de reducción de sustrato (SRT) equilibra la producción de glucoesfingolípidos con la capacidad catabólica residual de la enzima defectuosa, sin necesidad de restaurar la actividad enzimática directamente. La penetración demostrada de Miglustat en la barrera hematoencefálica —con concentración detectable en líquido cefalorraquídeo— es especialmente relevante para enfermedades con afectación neurológica.

La enfermedad de Tay-Sachs es causada por deficiencia de β-hexosaminidasa A (gen HEXA), lo que conduce a acumulación tóxica de gangliósido GM2 predominantemente en neuronas del sistema nervioso central. La ruta de biosíntesis del GM2 sigue la secuencia: ceramida → **glucosilceramida** (punto de inhibición de GCS por Miglustat) → lactosilceramida → GM3 → GM2. Al intervenir en el paso de GCS, Miglustat reduce el flujo metabólico hacia GM2; el efecto es mayor en formas de inicio tardío y juvenil, donde persiste actividad enzimática residual que puede compensar una acumulación reducida del sustrato.

La conexión entre la indicación original (Gaucher tipo 1: acumulación directa de glucosilceramida) y la nueva indicación (Tay-Sachs: acumulación de GM2 derivado de glucosilceramida) es directa y compartida en la misma vía de síntesis de glucoesfingolípidos. Es la predicción con mayor respaldo mecanístico en este paquete de evidencia, confirmada por estudios en modelos animales (ratones Tay-Sachs) que demostraron prevención del almacenamiento lisosómico, y por ensayos clínicos en humanos que validaron la penetración al SNC del fármaco.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fase 2 | Completado | 5 | Farmacocinética y tolerabilidad de Miglustat en GM2 gangliosidosis juvenil en dosis única y múltiple; estableció el perfil PK de referencia para diseño de dosis en población pediátrica |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fase 3 | Completado | 10 | PK, seguridad y tolerabilidad en GM2 gangliosidosis infantil clásica (Tay-Sachs y Sandhoff); detectó concentración significativa del fármaco en LCR y efecto sobre macrocefalia |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fase 3 | Terminado | 30 | Evaluación de efectos terapéuticos en formas infantiles de Sandhoff y Tay-Sachs; terminado prematuramente antes de completar la meta de inscripción, señal de eficacia limitada en fenotipo infantil |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Fase 2 | Reclutando | 21 | Estudio a largo plazo de Nizubaglustat en GM2 gangliosidosis o Niemann-Pick tipo C; incluye cohorte de transición desde tratamiento previo con Miglustat, referencia al ecosistema terapéutico actual |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fase 4 | Terminado | 16 | Régimen combinado Miglustat + dieta cetogénica en gangliosidosis infantil y juvenil; terminado, diseño combinado presentó dificultades de implementación sin atribuirse a señal negativa de Miglustat como monoterapia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revisión Sistemática | European Journal of Neurology | Evaluación sistemática de eficacia y seguridad de Miglustat en GM2 gangliosidosis; resultados inconsistentes entre estudios, especialmente entre formas infantiles (menor respuesta) y de inicio tardío |
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | ECA (Fase 2) | Genetics in Medicine | Estudio controlado aleatorizado de 12 meses más 24 meses de extensión en Tay-Sachs de inicio tardío (LOTS); evaluó seguridad y eficacia clínica como evidencia de mayor calidad disponible |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Revisión Narrativa | Int J Molecular Sciences | Revisión completa de características clínicas, fisiopatología y terapias actuales de GM2 gangliosidosis incluyendo estado de SRT |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revisión Narrativa | Frontiers in Physiology | Nuevos enfoques para Tay-Sachs: SRT, terapia génica y chaperonas; posiciona Miglustat como opción para formas no infantiles con actividad enzimática residual |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Serie de Casos | Neurology | SRT con Miglustat en 2 pacientes con Tay-Sachs infantil; no detuvo el deterioro neurológico pero confirmó penetración en LCR y efecto preventivo sobre macrocefalia |
| [9103204](https://pubmed.ncbi.nlm.nih.gov/9103204/) | 1997 | Preclínico | Science | Prevención del almacenamiento lisosómico en ratones Tay-Sachs con N-butyldeoxynojirimycin (precursor de Miglustat); evidencia seminal del concepto SRT en modelo animal |
| [12803928](https://pubmed.ncbi.nlm.nih.gov/12803928/) | 2003 | Preclínico | Phil Trans R Soc London B | Terapia de reducción de sustrato en modelos murinos de glucoesfingolipidosis incluyendo Tay-Sachs, Sandhoff y Fabry; fundamento preclínico de la clase terapéutica |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Observacional Longitudinal | Molecular Genetics and Metabolism | Historia natural de gangliosidosis infantiles; Miglustat señalado como limitado por efectos gastrointestinales y baja eficacia en formas de inicio infantil estricto |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Estudio Piloto | J Inherited Metabolic Disease | Pruebas neurocognitivas en Tay-Sachs de inicio tardío como medida de resultado para intervención terapéutica; valida herramienta para futuros ensayos |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Perfil de Fármaco | Current Opinion in Investigational Drugs | Perfil de Miglustat: mecanismo GCS, aprobación en Gaucher tipo 1 y desarrollo activo para Tay-Sachs, Fabry y Niemann-Pick tipo C |

---

## Información de Mercado en Colombia

Miglustat no cuenta con ningún registro sanitario vigente ante el INVIMA. El producto no está comercializado en Colombia en ninguna presentación. Para acceso terapéutico en el país se requeriría gestión de importación de medicamento no registrado bajo la figura de uso compasivo o importación por necesidad terapéutica no satisfecha, conforme a la normativa vigente del Ministerio de Salud.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Un ensayo controlado aleatorizado de Fase 2 completado y una revisión sistemática de 2023 respaldan el uso de Miglustat en Tay-Sachs de inicio tardío, con mecanismo de acción directamente derivado del uso aprobado en Gaucher tipo 1; sin embargo, los ensayos en formas infantiles muestran eficacia limitada y dos estudios fueron terminados prematuramente, lo que obliga a una selección cuidadosa del fenotipo del paciente antes de proceder.

**Para avanzar se necesita:**
- Identificar el mecanismo formal de acceso en Colombia: registro sanitario ante el INVIMA o importación por uso compasivo
- Determinar el fenotipo del paciente objetivo: las formas tardías y juveniles (con actividad enzimática residual de HexA) son las candidatas prioritarias; las formas infantiles clásicas muestran respuesta muy limitada
- Revisar el prospecto oficial de Zavesca® para datos completos de MOA, advertencias, contraindicaciones y perfiles de interacción
- Establecer plan de monitoreo de seguridad: efectos gastrointestinales frecuentes (diarrea, flatulencia, náuseas), temblor y parestesia periférica
- Evaluar el panorama competitivo emergente: Nizubaglustat (AZ-3102) se encuentra en Fase 2 para GM2 gangliosidosis y podría desplazar a Miglustat como estándar de cuidado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

